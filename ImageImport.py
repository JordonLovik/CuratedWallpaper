"""
    objective of imageimport is to:
    ask user for a list of urls
    verify url is good and will download
    store urls in list
    save urls to f.txt file for later use
"""
import urllib.request, urllib.error

list = []
listlenght = 2

def ImageImport():
    while len(list) < listlenght:
        item = input("enter urls: ")
        x = urllib.urlopen(item)
        x.getcode()
        print(x)
        if  x == "404":
            print(x)
            list.remove(item)
        if x == "200":
            print(x)
            list.remove(item)
        else:
            list.append(item)
        print(list)


ImageImport()
