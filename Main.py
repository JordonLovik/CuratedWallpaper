#import os is for make directory
import os, sys
#makes Directory if dosent already exist
directory = "c:\CuratedWallpaper"
path = directory.encode()
if not os.path.exists(path):
    os.makedirs(path)

