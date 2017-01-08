import urllib.request
from os.path import expanduser
import time
import os, sys
import ctypes

def main():
    delay = 2 #time delay between
    saveLocation = r"C:\CuratedWallpaper\1"

    directory = expanduser(r"~") + r"\Pictures" #directory is the home directory of computer plus /Picutres
    imagePath = directory + r"\Mario.bmp"

    #File with urls delimited by ','
    f = open(r'C:\CuratedWallpaper\f.txt', 'r')
    Urls = f.read().split('\n')
    f.close()

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

    #loop for saving images based on Urls array which is pulled from f.txt
    for item in Urls:
        filename = saveLocation + item.split('/')[-1]
        urllib.request.urlretrieve(item, filename)
        #outputString = path.abspath(filename)
        print(filename)
        print(item)
        #change BG after delay
        changeBG(filename)
        time.sleep(delay)
    else:
        pass
        #raise Exception("bad url")


    #webUrl.append(r"http://www.alsglobal.com/~/media/Images/Divisions/Life%20Sciences/Environmental/Houston.jpg")


    # makes diretory in C:\ if one is not already there
    makedir(directory)

    #urllib.request.urlretrieve ("http://www.emunix.emich.edu/~evett/GameProgramming/BookCode/chapter11.new/timedloop/background.bmp", imagePath)
    #http://www.pixelstalk.net/wp-content/uploads/2016/06/High-resolution-highres-pictures.jpg
    #http://www.alsglobal.com/~/media/Images/Divisions/Life%20Sciences/Environmental/Houston.jpg
    #http://wallpaper-gallery.net/images/high-resolution-images/high-resolution-images-20.gif
    #http://wallpaper-gallery.net/images/high-res-wallpaper/high-res-wallpaper-16.jpg
    #http://wallpaper-gallery.net/images/hi-res-wallpaper/hi-res-wallpaper-8.jpg
    #http://www.wearemoviegeeks.com/wp-content/uploads/WTCLibertyStatePark-HighRes-PhotoCreditErikaKoop-012.jpg

if __name__ == "__main__": main()