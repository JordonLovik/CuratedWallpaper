import urllib.request
from os.path import expanduser
import os
import time
import ctypes
import tkinter as tk
from tkinter import filedialog

#up next dowload image func implemented
#store local images to be referenced

def main():
    #takes root directory and adds given folders to it.

    dir = expanduser(r'~') + r'\Pictures\CuratedWallpaper'
    if not os.path.exists(dir):
        os.makedirs(dir)#make directoy if does not exist already
    #takes in directory location of files and adds prefix for saving local images to later
    saveLocation = dir + r'\CWP_'
    displayalbum = []  # array of file locations to be used to change BG

    root = tk.Tk()
    root.withdraw()
    urlfile_path = filedialog.askopenfilename()
    #urlfile = open(dir + r'\urlfile.txt', 'w') #previous open method
    urlfile = open(urlfile_path, 'r')
    urlslist = urlfile.read().split('\n') #line delimite urls and store in array
    urlfile.close()

    storefile = open(dir + r'\storefile.txt', 'w')
    if os.stat(dir + r'\storefile.txt').st_size != 0: #if storefile has data read it
        imagestore = storefile.read().split('\n')  # line delimite urls and store in array
    else:#if no data in imagestore create blank list
        imagestore = []
    running = True

    def checklink(imageurl):
        """takes in one url and checks it -
            returns true or false"""
        _imageurl = imageurl
        req = urllib.request.Request(_imageurl)
        req.get_method = lambda: 'HEAD'
        try:
            urllib.request.urlopen(req)
            #print('{} succeeded'.format(_imageurl))
            return True
        except urllib.request.HTTPError:
            #print('{} failed'.format(_imageurl))
            return False
    def changebg(imagepath):
        """takes in an image and sets background to it"""
        _imagepath = imagepath
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, _imagepath, 0)
        SPIF_UPDATEINIFILE = 0x2
    def downloadimage(imageurl, download = False):
        """takes in one image and downloads it - saves file string to displayalbum -
            stores list of downloaded images to list storefile.txt
                Use the Download flag False image has already been downloaded subverting
                    already downloaded images and storing into displayalbum"""
        filename = saveLocation + str(imageurl.split('/')[-1]) #Strip url to just the last element and add to savelocation
        if download == True:
            urllib.request.urlretrieve(imageurl, filename) #download url to savelocation + striped filename
            #print("Downloaded: " + imageurl + 'to: ' + filename)
        displayalbum.append(filename) #append File name to display array for changing BG later

    while running:
        # only run this for images that have not already been downloaded
        for i in urlslist:
            if i not in imagestore: # if image has already been dowloaded
                if checklink(i) == True: #if check is sucessfull download image
                    downloadimage(i, True)
                    imagestore.append(i)
                    storefile.write(i + '\n')
                else: pass #throw error to log and keep going
            else: #case the images have been downloaded before
                downloadimage(i, False)
        #print(imagestore)
        storefile.close()

        delay = input('Enter transition time desired: ')
        #setup delay here
        for j in displayalbum:
            #print(j)
            changebg(j)
            time.sleep(int(delay))
        #keep exicuting program?
        #answer = input("keep program running? y/n: ")
        #if answer == 'y':
            #pass
        #else:
            #running = False

if __name__ == '__main__': main()