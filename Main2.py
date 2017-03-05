import urllib.request
from os.path import expanduser
import time
import os
import ctypes
#up next dowload image func implemented
#store local images to be referenced

def main():

    def openfile(directory, filename, accesstype, delimiter='\n'):
        f = os.path.join(directory, filename)
        file = open(f, accesstype)
        filelist = file.read().split(delimiter)
        file.close()
        return filelist

    dir = expanduser(r'~') + r'\Pictures\CuratedWallpaper'
    saveLocation = dir + r'\CWP_'

    urls = openfile(dir, 'storefile.txt', 'r')

    urlfile = open(dir + r'\urlfile.txt', 'r')
    urlslist = urlfile.read().split('\n') #line delimite urls and store in array
    urlfile.close()

    storefile = open(dir + r'\storefile.txt', 'r+')
    imagestore = storefile.read().split('\n')  # line delimite urls and store in array

    running = True
    localimages = ["1cwp.jpg", "2cwp.jpg"]
    #imagestore = []

    """inicialize this list with downloadhistory.txt and save to it later on"""
    #downloadhistory [] = open(downloadhistory.txt)

    def checklink(imageurl):
        """takes in one url and checks it -
            returns true or false"""
        _imageurl = imageurl
        req = urllib.request.Request(_imageurl)
        req.get_method = lambda: 'HEAD'
        try:
            urllib.request.urlopen(req)
            print('{} succeeded'.format(_imageurl))
            return True
        except urllib.request.HTTPError:
            print('{} failed'.format(_imageurl))
            return False

    def changebg(imagepath):
        """takes in an image and sets background to it"""
        _imagepath = imagepath
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, _imagepath, 0)
        SPIF_UPDATEINIFILE = 0x2

    def downloadimage(image):
        """takes in one image and downloads it - saves file xcwp.jpg -
            stores list of downloaded images to list imagestore image"""
        #download image
        #save to location on computer
        #store location of image in list imagestore
        pass

    while running:
        # only run this for images that have not already been downloaded
        for j in urlslist:
            if j not in imagestore: # if image has already been dowloaded
                if checklink(j) == True: #if check is sucessfull download image
                    downloadimage(j)
                    imagestore.append(j)
                    storefile.write(j + '\n')
                else: pass #throw error to log and keep going
            else: pass

        #store already downloaded images to file
        print(imagestore)
        storefile.close()

        #setup delay here
        for x in imagestore:
            changebg(x)

        #keep exicuting program?
        answer = input("keep program running? y/n: ")
        if answer == 'y':
            pass
        else:
            running = False

if __name__ == '__main__': main()