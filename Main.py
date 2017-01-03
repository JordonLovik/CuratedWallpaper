import urllib.request
from os.path import expanduser
import time
import os, sys
import ctypes

def main():
    directory = expanduser(r"~") + r"\Pictures"
    imagePath = directory + r"\Mario.bmp"

    start = time.time()
    finish = time.time()


    #makes Directory if dosent already exist
    def makedir(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            return;
    #changes background based on imagePath
    def changeBG(imagePath):
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagePath , 0)
        SPIF_UPDATEINIFILE = 0x2
        return;

    #makes diretory in C:\ if one is not already there
    makedir(directory)

    #download an image to location
    urllib.request.urlretrieve ("http://www.emunix.emich.edu/~evett/GameProgramming/BookCode/chapter11.new/timedloop/background.bmp", imagePath)
    #http://www.pixelstalk.net/wp-content/uploads/2016/06/High-resolution-highres-pictures.jpg
    #http://www.alsglobal.com/~/media/Images/Divisions/Life%20Sciences/Environmental/Houston.jpg
    #http://wallpaper-gallery.net/images/high-resolution-images/high-resolution-images-20.gif
    #http://wallpaper-gallery.net/images/high-res-wallpaper/high-res-wallpaper-16.jpg
    #http://wallpaper-gallery.net/images/hi-res-wallpaper/hi-res-wallpaper-8.jpg
    #http://www.wearemoviegeeks.com/wp-content/uploads/WTCLibertyStatePark-HighRes-PhotoCreditErikaKoop-012.jpg

    #main program loop
    while finish - start > 10:
        imagePath = directory + r"\Water.jpg"
        changeBG(imagePath)
    else:
        imagePath = directory + r"\Mario.bmp"
        changeBG(imagePath)

    #takes in 1 argument: image file path and places it as background image
    changeBG(imagePath)

if __name__ == "__main__": main()