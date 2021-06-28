from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set() # 집합자료형으로 (중복x, 순서x)
random.seed(datetime.datetime.now())

#Retrieves a list of all Internal links found on a page
def getInternalLinks(bs, includeUrl): # 내부링크 : 같은 서버에 있는데, 페이지 주소만 다른 링크
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    #Finds all links that begin with a "/"
    for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')): # /가 앞에 오든지, ~~~~includeUrl이 앞에 오든지
                                '''
                                / => 상대주소는 내부링크이므로, 시작이 /인 것 모두 찾아냄
                                +includeUrl+ => 절대주소 중에서는 도메인주소 같으면 내부링크이므로, 도메인주소 같은 애들만 모두 찾아냄
                                             => 변수 includeUrl에 담긴 값을 정규표현식에 넣어주기 위함                                
                                '''
        if link.attrs['href'] is not None: # find_all 했을 때 하나 이상 존재해야 함
            if link.attrs['href'] not in internalLinks: # 한 번 들어갔던 링크는 중복적으로 들어가지 않음
                if(link.attrs['href'].startswith('/')): # 찾은 모든 링크 中 for문돌리고 있는 링크 하나가 /로 시작하는 상대주소이니?
                    internalLinks.append(includeUrl+link.attrs['href']) # 상대주소에 도메인주소를 더해 절대주소로 바꿔 리스트에 넣어줌
                else: # 찾은 모든 링크 中 for문돌리고 있는 링크 하나가 절대주소이니?
                    internalLinks.append(link.attrs['href'])
    return internalLinks
            
#Retrieves a list of all external links found on a page
def getExternalLinks(bs, excludeUrl): # 외부링크 : 아예 외부 서버에 있는, 서버 자체가 다른 링크
    externalLinks = []
    #Finds all links that start with "http" that do
    #not contain the current URL
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')): 
                                '''
                                ^(http|www) => 상대주소도 모두 내부링크이므로, 상대주소는 걸러내고 절대주소에서만 외부링크 찾아야 함
                                ((?!'+excludeUrl+').)* => 도메인주소 같으면 내부링크이므로, 도메인주소 다른 애들만 찾아야 함
                                '''
        if link.attrs['href'] is not None: # find_all 했을 때 하나 이상 존재해야 함
            if link.attrs['href'] not in externalLinks: # 한 번 들어갔던 링크는 중복적으로 들어가지 않음
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage) # startingPage 열어서 html 가져옴
    bs = BeautifulSoup(html, 'html.parser') # startingPage html 파싱 위한 객체 bs 만듦
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc) # bs가 갖고 있는 해당 html의 모든 externalLinks를 리스트로 담아옴
    if len(externalLinks) == 0: # externalLinks 하나도 없으면
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        '''
        URL의 일반적인 구조
            => 프로토콜://도메인주소/웹페이지주소/query(파라미터설정값같은것)
            => scheme://netloc/path;parameters?query#fragment
        urlparse(url).scheme → 프로토콜에 해당하는 부분 (http, https) 만 리턴 
        urlparse(url).netloc → 도메인주소에 해당하는 부분만 리턴
        '''
        internalLinks = getInternalLinks(bs, domain) # bs가 갖고 있는 해당 html의 모든 internalLinks를 리스트로 담아옴
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
        # internalLinks에서 랜덤으로(인덱스 랜덤으로 선택) 링크 하나 들어가서 externalLinks 하나라도 있어서 else문으로 빠질 때까지 재귀. 
    else: # externalLinks 하나라도 있으면
        return externalLinks[random.randint(0, len(externalLinks)-1)]
        # externalLinks에서 랜덤으로(인덱스 랜덤으로 선택) 링크 하나 뽑아 리턴
    
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite) # 외부 링크 하나 담김
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink) # 재귀함수. 찾아낸 외부 링크에 들어가서 또 다시 외부 링크 찾아냄
            
followExternalOnly('http://oreilly.com')