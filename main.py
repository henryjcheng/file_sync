'''
Date    02/26/21
Author  Henry Cheng
Status  Dev

This module move file from local project folder to shared drive.
Purpose is to be ran every Friday to upload any local work to shared drive as a backup.
'''
import os
import sys

path_source = sys.argv[1]
path_destination = sys.argv[2]

os.replace()
