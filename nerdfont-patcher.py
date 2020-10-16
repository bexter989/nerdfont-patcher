#!/usr/bin/python

import os
import sys


def src_dir_exists():
    ''' Bool: Checks if the src folder exists '''
    return os.path.isdir("./src/glyphs")


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
    with open("./font_names.txt", "r") as f:
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


def main(folder, name):
    ''' Font patching time! Go Drink a coffee. '''
    # Scan the folder passed in via script arg
    fonts = os.listdir(folder)

    # Loop over each item and patch the glyphs
    for i, font in enumerate(fonts):
        font_path = folder + os.sep + fonts[i]
        command = "fontforge -script font-patcher -s -w -c --no-progressbars --careful {} -out Patched/{}".format(
            font_path, name)
        os.system(
            command
        )


if __name__ == '__main__':
    # Get number of arguments
    arg_len = len(sys.argv)

    # We need two args
    if arg_len == 2:
        folders = sys.argv[1]
        name = sys.argv[2]

        # Create the src folder and download
        # all the font glyphs from the NerdFonts repo on first run
        if not src_dir_exists():
            os.makedirs("./src/glyphs")
            download_src_fonts()

        # Download the NerdFonts Patcher on first run
        if not patcher_exists():
            download_patcher()

        # Start the patcher
        main(folders, name)
    else:
        print("Almost did it..!\nI need two arguments. The Folder where the fonts are, and the name of the font to Patch")
        print("Like:\n  ${} ./Fonts/Agave Agave".format(sys.argv[0]))
