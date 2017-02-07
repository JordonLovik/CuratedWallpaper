"""
    objective of imageimport is to:
    ask user for a list of urls
    verify url is good and will download
    store urls in list
    save urls to f.txt file for later use
"""
import urllib.request, urllib.error
import urllib
import http.client

#list = []
#listlenght = 3

def is_downloadable(url):
    h = urllib.request.Request((url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        print("false")
        return False
    if 'html' in content_type.lower():
        print("false")
        return False
    print("True")
    return True

is_downloadable("http://wallpapercave.com/wp/46IcIP8.jpg")

"""
    def httpExists(url):
        host, path = urlparse.urlsplit(url)[1:3]
        found = 0
        try:
            connection = httplib.HTTPConnection(host)  ## Make HTTPConnection Object
            connection.request("HEAD", path)
            responseOb = connection.getresponse()  ## Grab HTTPResponse Object

            if responseOb.status == 200:
                found = 1
            else:
                print
                "Status %d %s : %s" % (responseOb.status, responseOb.reason, url)
        except Exception, e:
            print
            e.__class__, e, url
        return found

    def _test():
        import doctest, httpExists
        return doctest.testmod(httpExists)


"""
#objective take a url test to see if it is accpetable then add it to file coma delimited