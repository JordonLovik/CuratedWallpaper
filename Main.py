import urllib.request
from os.path import expanduser
import time
import os
import ctypes

def main():
    delay = 1

    #for some reason th user input causes errors
    #UserInput1 = int(input("Enter desired delay: "))
    #print(UserInput1, type(UserInput1))
    #delay = UserInput1

    #Global Variables
    #directory = expanduser(r"~") + r"\Pictures"
    directory = expanduser(r"~") + r"\Pictures\CuratedWallpaper"
    print (directory)
    #saveLocation = r"C:\CuratedWallpaper\1"
    saveLocation = directory + r"\CWP_"
    localFiles = []

    #f = open(r'C:\CuratedWallpaper\f.txt', 'r')
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