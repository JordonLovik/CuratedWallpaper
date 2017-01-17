"""
    objective of imageimport is to:
    ask user for a list of urls
    verify url is good and will download
    store urls in list
    save urls to f.txt file for later use
"""
import urllib.request, urllib.error
import http.client

list = []
listlenght = 3





def ImageImport():
    while len(list) < listlenght:
        print(len(list))
        item = input("enter urls: ")
        c = http.client.HTTPSConnection(item)
        c.request("HEAD", "/")
        res = c.getresponse()
        #print(res.status, res.reason)
        data = res.reason
        print(list)
        #if state just wont work
        if data == "OK":
            list.pop()
        else:
            list.append(item)

ImageImport()