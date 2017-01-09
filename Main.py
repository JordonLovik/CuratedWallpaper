import urllib.request
from os.path import expanduser
import time
import os, sys
import ctypes

def main():
    delay = 2 #time delay between
    saveLocation = r"C:\CuratedWallpaper\1"

    #directory is the home directory of computer plus /Picutres
    directory = expanduser(r"~") + r"\Pictures"

    #File with urls delimited by ','
    f = open(r'C:\CuratedWallpaper\f.txt', 'r')
    Urls = f.read().split('\n')
    f.close()

    #makes Directory if dosent already exist
    def makedir(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            return;
    #changes background based on Path
    def changeBG(Path):
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, Path , 0)
        SPIF_UPDATEINIFILE = 0x2
        return;
    # makes diretory in C:\ if one is not already there
    makedir(directory)

    #loop for saving images based on Urls array which is pulled from f.txt
    for item in Urls:
        filename = saveLocation + item.split('/')[-1]
        urllib.request.urlretrieve(item, filename)
        #outputString = path.abspath(filename)
        print(filename)
        print(item)
        changeBG(filename)
        time.sleep(delay)
    else:
        pass
        #raise Exception("bad url")

if __name__ == "__main__": main()