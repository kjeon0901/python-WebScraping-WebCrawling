from urllib.request import urlopen
from bs4 import BeautifulSoup

######### 재귀횟수 9번 (처음 실행까지 10번) => 웹페이지 10개 크롤링할 것임. 
######### kevin bacon 위키백과 Contents 목차 1순위들만을 crawling해서 목차에 대한 데이터를 리스트로 담기
######### [페이지제목(Kevin Bacon), Contents 1., Contents 2., Contents 3.] 이거 10개를 또 큰 리스트에 담기

pages = set()
recursion = 9
total_contents = []
def getLinks(pageUrl):
    global pages
    global recursion
    global total_contents
    if recursion==-1:
        return
    if recursion <9:
        print("=============== 재귀", 9-recursion, "===============")

    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    contents = []
    try: # 목차 리스트 담기
        contents.append(bs.h1.get_text())
        print(bs.find('div', {'class':"toctitle"}).next_siblings)
        #for child in bs.find('div', class_="toctitle").next_siblings.li.a.get_text():
        #    print(child)
        #    contents.append(bs.find('a').get_text())
    except AttributeError:
        print('This page is missing something! Continuing.')
    print(contents)
    total_contents.append(contents)
    
    for link in bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            if '(disambiguation)' in link.attrs['href']:
                continue
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                recursion-=1
                return getLinks(newPage) # 재귀함수. 
            
getLinks('/wiki/Kevin_Bacon')