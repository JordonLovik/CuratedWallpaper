import urllib.request
from os.path import expanduser
import time
import os, sys
import ctypes

def main():
    delay = 0.5
    saveLocation = r"C:\CuratedWallpaper\1"
    localFiles = []
    #directory is the home directory of computer plus /Picutres
    directory = expanduser(r"~") + r"\Pictures"

    f = open(r'C:\CuratedWallpaper\f.txt', 'r')
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

    makedir(directory)

    #in this loop check to see if local file already exsists before doing the urllib.request

    #loop for saving images based on Urls array which is pulled from f.txt
    for i in Urls:
        filename = saveLocation + i.split('/')[-1]
        localFiles.append(filename)
        urllib.request.urlretrieve(i, filename)
        #print(filename)
        #print(i)
    else:
        pass
        #raise Exception("bad url")

    for i in localFiles:
        changeBG(i)
        time.sleep(delay)

if __name__ == "__main__": main()