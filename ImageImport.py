"""
    objective of imageimport is to:
    ask user for a list of urls
    verify url is good and will download
    store urls in list
    save urls to f.txt file for later use
"""
import urllib.request

def is_downloadable(url):
    _url = url
    req = urllib.request.Request(_url)
    req.get_method = lambda: 'HEAD'
    try:
        urllib.request.urlopen(req)
        print('sucess')
        return True
    except urllib.request.HTTPError:
        print('failure at: {}' .format(_url))
        return False

urllist = ["http://wallpapercave.com/wp/46IcIP8.jpg","http://wallpapercave.com/wp/46IcIP8.jpg","http://wallpapercave.com/wp/46IcIP8.jpg2","http://wallpapercave.com/wp/46IcIP8.jpg"]
goodlist = []
for i in urllist:
    check = is_downloadable(i)
    if check == True:
        goodlist.append(i)
    else:
       print('an error occured when accessing a url')

print(goodlist)