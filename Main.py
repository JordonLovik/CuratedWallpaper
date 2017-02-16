import urllib.request
from os.path import expanduser
import time
import os
import ctypes

def main():
    #
    #Global Variables
    directory = expanduser(r'~') + r'\Pictures\CuratedWallpaper'
    saveLocation = directory + r'\CWP_'
    delay = 1
    localFiles = []
    goodurllist = []

    f = open(directory + r'\f.txt', 'r')
    Urls = f.read().split('\n')
    f.close()


    def makedir(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
    def changeBG(Path):
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, Path , 0)
        SPIF_UPDATEINIFILE = 0x2
    def downloadimages(imageurls):
        print('*downloading*')
        _countertotal = len(imageurls)
        _counter = 0
        for i in imageurls:
            filename = saveLocation + i.split('/')[-1]
            localFiles.append(filename)
            urllib.request.urlretrieve(i, filename)
            _counter = _counter + 1
            print("Downloading: {} of {}".format(_counter, _countertotal))

    def is_downloadable(url):
        _url = url
        req = urllib.request.Request(_url)
        req.get_method = lambda: 'HEAD'
        try:
            urllib.request.urlopen(req)
            print('{} succeeded'.format(_url))
            return True
        except urllib.request.HTTPError:
            print('{} failed'.format(_url))
            return False

    print('*testing downloadability*')
    for i in Urls:
        check = is_downloadable(i)
        if check == True:
            goodurllist.append(i)

    makedir(directory)
    downloadimages(goodurllist)
    #downloadimages(Urls) to see is_downloadable working

    for i in localFiles:
        changeBG(i)
        time.sleep(delay)

if __name__ == '__main__': main()

