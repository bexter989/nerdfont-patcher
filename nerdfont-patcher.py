#!/usr/bin/env python
# -*- coding: utf-8 -*-
#TODO: Use threading to improve patching times

import os
import sys
import re



def folder_exists(folder):
    ''' Bool: Checks if a folder exists '''
    return os.path.isdir(folder)


def patcher_exists():
    ''' Bool: Checks if the NerdFonts patcher script exists '''
    return os.path.isfile("./font-patcher")


def download_patcher():
    ''' Downloads the Nerd Fonts Patcher script '''
    print("Downloading NerdFonts Patcher Script")
    command = "curl -s -L https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/font-patcher --output font-patcher"
    os.system(command)


def download_src_fonts():
    ''' Downloads Glyph source files from the Nerd Fonts Repo '''
    with open("font_names.txt", "r") as f:
        print("Downloading glyph source fonts\n")
        for font_name in f.readlines():

            # Removes \r\n or crlf
            font_name = font_name.rstrip()

            # Skips the comments in the font_names.txt
            if "#" in font_name:
                continue

            # User feedback
            print("Downloading {}".format(font_name))
            command = "curl -s -L 'https://github.com/ryanoasis/nerd-fonts/blob/master/src/glyphs/*?raw=true' --output 'src/glyphs/*'".replace(
                "*", font_name)
            os.system(command)


def fix_filenames_in(folder):
    ''' (ง '̀͜ '́ )ง Removes spaces from filenames within a folder '''
    # NOTE: Shorter signature from Core Kramer StackOverflow
    # https://stackoverflow.com/questions/64468635/is-there-a-better-way-to-replace-multiple-spaces-in-file-names
    files = os.listdir(folder)

    for file_name in files:
        new_name = ''.join([re.sub(r'\s+', '-', i) for i in file_name])
        old_filename = folder + os.sep + file_name
        new_filename = folder + os.sep + new_name
        os.rename(old_filename, new_filename)


def patch(folder, name):
    ''' Font patching time! (•̀o•́)ง Go Drink a coffee. '''
    # Scan the folder passed in via script arg
    fix_filenames_in(folder)
    fonts = os.listdir(folder)

    # Loop over each item and patch the glyphs
    for i, _ in enumerate(fonts):

        # If it's not a font, we don't want it
        if (not "ttf" in fonts[i]) and (not "otf" in fonts[i]):
            print("Not a font... Moving along")
            continue

        # Font path
        font_path = folder + os.sep + fonts[i]

        # This will patch everything. Powerline, Weather icons, FontAwesome... EVERYTHING!
        # It takes a while to patch fonts so get a coffee while waiting. Oh! and the '-w 'switch is for
        # Windows compatibility.. Something about limiting the number of characters in the font name.
        print("Patching {}".format(fonts[i]))
        command = "fontforge -script ." + os.sep + "font-patcher -s -q -w -c --no-progressbars --careful {} -out Patched" + os.sep + "{}".format(
            font_path, name)
        os.system(command)


if __name__ == '__main__':
    # Get number of arguments
    arg_len = len(sys.argv)

    # We need two args
    if arg_len > 1:
        font_folder, name = sys.argv[1:]

        # Create the src folder and download all the font glyphs from the NerdFonts repo on first run
        if not folder_exists("." + os.sep + "src" + os.sep + "glyphs"):
            os.makedirs("." + os.sep + "src" + os.sep + "glyphs")
            download_src_fonts()

        # Create a folder based on the name param for the fonts
        if not folder_exists('.' + os.sep + 'Patched' + os.sep + '{}'.format(name)):
            os.makedirs('.' + os.sep + 'Patched' + os.sep + '{}'.format(name))

        # Download the NerdFonts Patcher on first run
        if not patcher_exists():
            download_patcher()

        # Start the patcher
        patch(font_folder, name)
        print("(⌐■_■) Done!")
    else:
        print("\n")
        print("+------------------------------------------------------+")
        print("| ¯\_(ツ)_/¯            Whoopss!              (ง '̀͜ '́ )ง  |")
        print("+------------------------------------------------------+\n")
        print("Almost did it..! I need two arguments.\n\n1) The Folder where the fonts are, and\n2) The name of the font to Patch\n")
        print("Like:\n > {} ./Fonts/Agave Agave\n\n".format(sys.argv[0]))
