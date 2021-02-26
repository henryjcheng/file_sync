'''
Date    02/26/21
Author  Henry Cheng
Status  Dev

This module move file from local project folder to shared drive.
Purpose is to be ran every Friday to upload any local work to shared drive as a backup.
'''
import sys, os, shutil, glob

path_source = sys.argv[1]
path_destination = sys.argv[2]

print(os.listdir(path_source))
print(os.path.join(path_source, '*.*'))
print(glob.glob(path_source))

for file in glob.glob(path_source):
    shutil.copy2(file, path_destination)
