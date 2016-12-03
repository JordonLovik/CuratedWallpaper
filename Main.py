import urllib.request
import os, sys
import ctypes

directory = "c:\CuratedWallpaper"


#makes Directory if dosent already exist
def makedir(directory):
    folderpath = directory.encode()
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        return;

makedir(directory)

urllib.request.urlretrieve ("http://www.emunix.emich.edu/~evett/GameProgramming/BookCode/chapter11.new/timedloop/background.bmp", "\CuratedWallpaper\Mario.bmp")

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "c:\CuratedWallpaper\Mario.bmp" , 0)