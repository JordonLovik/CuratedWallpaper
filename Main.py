import urllib.request
from os.path import expanduser
import time
import os
import ctypes

def main():
    delay = 1

    #for some reason th user input causes errors
    #UserInput1 = int(input("Enter desired delay: "))

    #Global Variables
    directory = expanduser(r"~") + r"\Pictures\CuratedWallpaper"
    saveLocation = directory + r"\CWP_"
    #localFiles is defined globally  so that its acceptable by multiple funtions
    localFiles = []

    #download the config file for web images)
    f = open(directory + r"\f.txt", 'r')
    Urls = f.read().split('\n') # clean this up
    f.close()
    dow = 0

    def makedir(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
    def changeBG(Path):
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, Path , 0)
        SPIF_UPDATEINIFILE = 0x2
    def DownloadImages(imageUrls,number):
        for i in imageUrls:
            filename = saveLocation + i.split('/')[-1]
            localFiles.append(filename)
            urllib.request.urlretrieve(i, filename)
            number = number + 1
            print(number)

    makedir(directory)
    DownloadImages(Urls, dow)

    for i in localFiles:
        changeBG(i)
        time.sleep(delay)
        #test

if __name__ == "__main__": main()