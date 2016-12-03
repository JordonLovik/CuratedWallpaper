import urllib.request
import os, sys
import ctypes

directory = "c:\CuratedWallpaper"
imagePath = directory + "Mario.bmp"

#makes Directory if dosent already exist
def makedir(directory):
    folderpath = directory.encode()
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        return;

def changeBG(imagePath):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imagePath , 0)
    return;

#makes diretory in C:\ if one is not already there
makedir(directory)

#takes in 1 argument: image file path and places it as background image
changeBG(imagePath)

#download an image
urllib.request.urlretrieve ("http://www.emunix.emich.edu/~evett/GameProgramming/BookCode/chapter11.new/timedloop/background.bmp", "\CuratedWallpaper\Mario.bmp")
