from datetime import datetime
import shutil, os

folder = input('Choose a folder to rename the files of (e.g. files1/files2)... ')
now = datetime.now()

for root, dirs, files in os.walk(folder):
    for name in files:
        path = folder + '/' + name
        new_name = path[:-4] + now.strftime("_%d-%m-%Y_%H-%M") + path[-4:]
        print('renaming ' + path + ' to ' + new_name)
        shutil.move(path, new_name)
