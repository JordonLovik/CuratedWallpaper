import urllib.request
from os.path import expanduser
import os, sys
import ctypes

#directory = "c:\CuratedWallpaper"
directory = expanduser(r"~") + r"\Pictures"
print (directory)

imagePath = directory + r"\Mario.bmp"
#changePath is for debugging only
#changePath = "c:\CuratedWallpaper\8.jpg"
#imagePath2 = imagePath.encode()
#check to see whats inside imagePath

print (imagePath)
#makes Directory if dosent already exist
def makedir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        return;

#need to change path to variable
def changeBG(imagePath):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagePath , 0)
    SPIF_UPDATEINIFILE = 0x2
    return;

#makes diretory in C:\ if one is not already there
makedir(directory)

#download an image to location
#urllib.request.urlretrieve (r"http://www.emunix.emich.edu/~evett/GameProgramming/BookCode/chapter11.new/timedloop/background.bmp", imagePath)

#takes in 1 argument: image file path and places it as background image
changeBG(imagePath)
print
print ("imagePath var " + imagePath)
#print ("changePath var " + changePath)