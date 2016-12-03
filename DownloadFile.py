#downloadimage from url
import urllib.request


website ="http://www.digimouth.com/news/media/2011/09/google-logo.jpg"
#encode the following string because urllib.request does not like '/' characters
LocalDir = "\CuratedWallpaper\Wallpaper.jpg"
LocalDir2 = LocalDir.encode()
urllib.request.urlretrieve(website, LocalDir2)