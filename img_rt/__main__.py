import os
import sys
from .rtf import rtf
from .any2jpeg import any2jpeg


def print_help():
    text = '''Usage:\timg_refactor MODE [-f src_folder] [-o dst_folder]

Modes:
\trtf\t\trestore original extensions
\tto-jpg\t\tconvert all images to jpeg

Options:
\t-f\t\tfull path to source folder (default: current folder)
\t-o\t\tfull path to destination folder (default: \'\\output\' in source folder)

NOTE:
\t \"-o none\" means \"do not make any destination folder\"'''
    print(text)


def print_error():
    text = 'ERROR:\texample - img_refactor rtf\ntry:\timg_refactor --help'
    print(text)


def main(*args):
    if len(args[0]) == 1:
        print_error()
        quit()
    elif len(args[0]) == 2:
        if args[0][1] == '-h' or args[0][1] == '--help':
            print_help()
            quit()
        elif args[0][1] == 'rtf':
            rtf(os.getcwd(), 'output')
            quit()
        elif args[0][1] == 'to-jpg':
            any2jpeg(os.getcwd(), 'output')
            quit()
        else:
            print_error()
    elif len(args[0]) == 4:
        if args[0][1] == 'rtf':
            if args[0][2] == '-f':
                rtf(args[0][3], 'output')
                quit()
            elif args[0][2] == '-o':
                rtf(os.getcwd(), args[0][3])
                quit()
        elif args[0][1] == 'to-jpg':
            if args[0][2] == '-f':
                any2jpeg(args[0][3], 'output')
                quit()
            elif args[0][2] == '-o':
                any2jpeg(os.getcwd(), args[0][3])
                quit()
        else:
            print_error()
    elif len(args[0]) == 6:
        if args[0][2] == '-f' and args[0][4] == '-o':
            if args[0][1] == 'rtf':
                rtf(args[0][3], args[0][5])
                quit()
            elif args[0][1] == 'to-jpg':
                any2jpeg(args[0][3], args[0][5])
                quit()
            else:
                print_error()
        else:
            print_error()
    else:
        print_error()


if __name__ == '__main__':
    main(sys.argv)
