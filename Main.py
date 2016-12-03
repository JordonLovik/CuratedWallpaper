import urllib.request
import os, sys

directory = "c:\CuratedWallpaper"

#makes Directory if dosent already exist
def makedir(directory):
    folderpath = directory.encode()
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        return;

makedir(directory)

urllib.request.urlretrieve ("http://wallpapercave.com/wp/hUukl3e.jpg", "\CuratedWallpaper\Mariobg.jpg")

