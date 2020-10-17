#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

def rename_them(folder):
    files = os.listdir(folder)

    for file in files:
        new, old = '', ''
        old = file

        if " " in file:
            new = file.split(" ")
            new = [item for item in new if not item == '']
            new = '-'.join(new)

        if new == '':
            new = 'New: No change'
        print(new, ' | ', old)
        oldfile = folder + os.sep + file
        newfile = folder + os.sep + new
        os.rename(oldfile,newfile)


if __name__ == '__main__':
    len_args = len(sys.argv)

    if len_args > 1:
        folder = sys.argv[1]
        rename_them(folder)
