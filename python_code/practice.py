import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'

def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
    elif source.startswith('https://www.'):
        url = 'http://{}'.format(source[12:])
    elif source.startswith('http://'):
        url = source
    elif source.startswith('https://'):
        url = 'http://{}'.format(source[8:])
    elif source.startswith('www.'):
        url = 'http://{}'.format(source[4:])
    else:
        url = '{}/{}'.format(baseUrl, source) 
    return url 

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '') 
    external = re.compile('.*\.com').search(path) 
    if external != None:
        path = path.replace(external.group(), '')
    path = downloadDirectory+path 
    directory = os.path.dirname(path) 

    if not os.path.exists(directory):
        os.makedirs(directory)
    print(path)
    return path

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.body.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download['src']) 
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))    
