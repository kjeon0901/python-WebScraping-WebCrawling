import os # 내 컴퓨터 안의 경로로 이동한다거나, 폴더를 만든다거나 하는 행위 가능
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com' # 도메인주소이자, 우리가 scraping할 웹페이지

def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'): # startswith('str') : source를 전부 string의 관점에서 봤을 때, string이 'str'로 시작하는가?
        url = 'http://{}'.format(source[11:])
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = 'http://{}'.format(source[4:])
    else: # source가 상대경로라면
        url = '{}/{}'.format(baseUrl, source) # 도메인주소와 합쳐줌
    if baseUrl not in url:
        return None
    return url # 결과적으로, 전부 http://로 시작하고 www.는 없는 꼴로 바꿔줌

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.', '') # 아까 getAbsoluteURL( )에서 이미 다 없애줬기 때문에 의미 없는 코드임
    path = path.replace(baseUrl, '') # 도메인주소 포함되어 있으면 없애줌 (내 컴퓨터의 디렉토리에 저장해야 하니까) => "상대경로만 남음!!"
    path = downloadDirectory+path # 'downloaded' + 상대경로 => 저장 경로 완성
    directory = os.path.dirname(path) # path에서 directory만 담음

    if not os.path.exists(directory): # directory(폴더)가 존재하지 않으면
        os.makedirs(directory) # directory(폴더) 새로 만들어줌

    return path

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.findAll(src=True) # src라는 속성값을 가지고 있는 모든 태그    // script에서 쓰인 건 제외되니까, 총 3개의 img파일만 담김

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download['src']) # getAbsoluteURL( ) 메소드 : 서버 상에 저장된 이미지 파일 경로가 담김
    if fileUrl is not None: # 존재하면
        print(fileUrl)

urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
'''
어떤 파일을 fileUrl에서 다운받아주세요. 
그리고 현재 작업 경로에서 'downloaded'라는 폴더를 만들고, 폴더 안에서 fireUrl 상대 경로와 똑같은 경로에 그 파일을 저장해주세요. 
'''
