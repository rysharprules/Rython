from datetime import datetime
import shutil, os

def rename(path, type, new_name):
    print('renaming ' + type + ' ' + path + ' to ' + new_name)
    shutil.move(path, new_name)

folder = input('Choose a folder to rename the contents (files and folders) of (e.g. files3)... ')
now = datetime.now().strftime("_%d-%m-%Y_%H-%M")

for root, dirs, files in os.walk(folder):
    for name in files:
        path = os.path.join(root, name)
        rename(path, 'file', path[:-4] + now + path[-4:])
for root, dirs, files in os.walk(folder): # new loop required otherwise sub-dir is renamed before sub-dir files which invalidates the orignal path
    for dir in dirs:
        path = os.path.join(root, dir)
        rename(path, 'directory', path + now)