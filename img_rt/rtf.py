import os
import sys
import imghdr
import shutil


def isIMG(path_to_img):
    ext = ['.png', '.jpg', '.jpeg', '.webp', '.gif']
    _, extension = os.path.splitext(path_to_img)
    return extension.lower() in ext


def copy_files(path, new_path, prefix=''):
    files = (file for file in os.listdir()
             if isIMG(os.path.join(path, file)))
    for file in files:
        shutil.copy2(os.path.join(path, file),
                     os.path.join(new_path, prefix+file))
    print('Files copied into', new_path)


def rename_files(path):
    files = (file for file in os.listdir()
             if os.path.isfile(os.path.join(path, file)))
    for file in files:
        old_name = os.path.join(path, file)
        name, extension = os.path.splitext(old_name)
        if imghdr.what(old_name) == None:
            new_name = os.path.join(path, '.UNKNOWN.'+file)
        else:
            new_name = name+'.'+imghdr.what(old_name)
        try:
            os.rename(old_name, new_name)
        except FileExistsError:
            os.remove(old_name)
    print('Files renamed!')


def rtf(path, new_path):
    os.chdir(path)
    if new_path == 'none':
        copy_files(path, path, '.renamed.')
        rename_files(path)
        print('Done!')
        quit()
    if new_path == 'output':
        new_path = os.path.join(path, new_path)
    try:
        os.mkdir(new_path)
    except FileExistsError:
        if input('Output folder already exists! Continue? (y/n) ') == 'y':
            copy_files(path, new_path)
            rename_files(new_path)
        else:
            quit()
    else:
        copy_files(path, new_path)
        rename_files(new_path)
    print('Done!')
