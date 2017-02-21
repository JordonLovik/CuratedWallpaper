import urllib.request
from os.path import expanduser
import time
import os
import ctypes

def main():
    running = True
    urls = ["1cwp.com", "1cwp.com"]
    localimages = ["1cwp.jpg", "2cwp.jpg"]
    imagestore = 'oneimagefile'

    """inicialize this list with downloadhistory.txt and save to it later on"""
    #downloadhistory [] = open(downloadhistory.txt)

    def checklink(imageurl):
        """takes in one url and checks it - stores good urls in list -
            returns true or false"""
        #takes in single image url
        #does true false check
        #passes results
        pass
    def changebg(image):
        """takes in an image and sets background to it"""
        #change Background
        pass
    def downloadimage(image):
        """takes in one image and downloads it - saves file xcwp.jpg -
            stores list of downloaded images to list imagestore image"""
        #download image
        #save to location on computer
        #store location of image in list imagestore
        pass

    while running:

        # only run this for images that have not already been downloaded
        for j in urls:
            #if j !in downloadhistory:
                if checklink(j) == True: #if check is sucessfull download image
                    downloadimage(j)
                    # save downloadimage(j) to file downloadhistory.txt
                else: pass #throw error to log and keep going

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