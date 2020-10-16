#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from sys import platform


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
            font_name = font_name.rstrip()

            # Skips the comments in the font_names.txt
            if "#" in font_name:
                continue

            # User feedback
            print("Downloading {}".format(font_name))
            command = "curl -s -L 'https://github.com/ryanoasis/nerd-fonts/blob/master/src/glyphs/*?raw=true' --output 'src/glyphs/*'".replace(
                "*", font_name)
            os.system(command)


def patch(folder, name):
    ''' Font patching time! Go Drink a coffee. '''
    # Scan the folder passed in via script arg
    fonts = os.listdir(folder)

    # Loop over each item and patch the glyphs
    for i, _ in enumerate(fonts):

        # If it's not a font, we don't want it
        if not ".ttf" or ".otf" in fonts[i]:
            continue

        # "¯\_(ツ)_/¯"
        font_path = folder + os.sep + fonts[i]

        # This will patch everything. Powerline, Weather FontAwesome... EVERYTHING!
        # It takes a while to patch sh get a coffee and relax

        if platform == "linux" or platform == "linux2" or platform == "darwin":
            command = "fontforge -script ./font-patcher -s -c --no-progressbars --careful {} -out Patched/{}".format(
                font_path, name)
        else:
            command = "fontforge -script .\\font-patcher -s -w -c --no-progressbars --careful {} -out Patched/{}".format(
                font_path, name)
        os.system(
            command
        )


if __name__ == '__main__':
    # Get number of arguments
    arg_len = len(sys.argv)

    # We need two args
    if arg_len > 1:
        folders, name = sys.argv[1:]

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
        patch(folders, name)
    else:
        print("¯\_(ツ)_/¯")
        print("Almost did it..!\nI need two arguments. The Folder where the fonts are, and the name of the font to Patch")
        print("Like:\n  ${} ./Fonts/Agave Agave".format(sys.argv[0]))
