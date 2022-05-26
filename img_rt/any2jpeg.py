import os
import sys
import imghdr
import shutil
from PIL import Image


def isIMG(path_to_img):
    ext = ['.png', '.jpg', '.jpeg', '.webp']
    _, extension = os.path.splitext(path_to_img)
    return extension.lower() in ext


def convert_files(path, new_path, clear=False):
    files = (file for file in os.listdir(path)
             if os.path.isfile(os.path.join(path, file)))
    for file in files:
        old_name = os.path.join(path, file)
        name, extension = os.path.splitext(file)
        new_name = os.path.join(new_path, name+'.jpg')

        im1 = Image.open(old_name)
        rgb_im = im1.convert('RGB')
        rgb_im.save(new_name)

    print('Files converted!')


def any2jpeg(path, new_path):
    os.chdir(path)
    if new_path == 'output':
        new_path = os.path.join(path, new_path)
    try:
        os.mkdir(new_path)
    except FileExistsError:
        if input('Output folder already exists! Continue? (y/n) ') == 'y':
            convert_files(path, new_path)
        else:
            quit()
    else:
        convert_files(path, new_path)
    print('Done!')
