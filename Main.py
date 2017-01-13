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
    print (directory)
    saveLocation = directory + r"\CWP_"
    localFiles = []

    #download the config file for web images
    #urllib.request.urlretrieve(r"https://drive.google.com/open?id=1oIaJ49u4f5kgTwojGqHhDW_wawLGcgjoT1qra24ADLc", directory + r"\f.txt")
    f = open(directory + r"\f.txt", 'r')
    Urls = f.read().split('\n')
    f.close()

    def makedir(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            return;
    def changeBG(Path):
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, Path , 0)
        SPIF_UPDATEINIFILE = 0x2
        return;
    def DownloadImages(imageUrls):
        for i in imageUrls:
            filename = saveLocation + i.split('/')[-1]
            localFiles.append(filename)
            urllib.request.urlretrieve(i, filename)
            #print(filename)
            #print(i)
        else:
            pass
            #raise Exception("bad url")

    makedir(directory)
    DownloadImages(Urls)

    #while loop will replace for loop in final program
    for i in localFiles:
        changeBG(i)
        time.sleep(delay)

if __name__ == "__main__": main()