## Crawling Sites through Links

# Quiz. business 섹션의 기사들만 print

import requests
from bs4 import BeautifulSoup

#ln [1] :

class Website:

    def __init__(self, name, url, targetPattern, absoluteUrl, titleTag, bodyTag):
        self.name = name # 사이트 이름
        self.url = url # 사이트 도메인 주소
        self.targetPattern = targetPattern # 찾아야 하는 href 패턴 (정규표현식)
        self.absoluteUrl = absoluteUrl # 절대주소 : True, 상대주소 : False
        self.titleTag = titleTag # 링크 내부 title 위치 찾는 태그
        self.bodyTag = bodyTag # 링크 내부 body 위치 찾는 태그


class Content:

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print('URL: {}'.format(self.url))
        print('TITLE: {}'.format(self.title))
        print('BODY:\n{}'.format(self.body))


#ln [2] :

import re


class Crawler:
    def __init__(self, site):
        self.site = site
        self.visited = []

    def getPage(self, url):
        try:
            req = requests.get(url) # url에 해당하는 html 가져옴
        except requests.exceptions.RequestException:
            return None # 에러나면 None 리턴
        return BeautifulSoup(req.text, 'html.parser') # 그 html을 파싱하기 위한 bs 객체 리턴

    def safeGet(self, pageObj, selector):
        selectedElems = pageObj.select(selector) 
        if selectedElems is not None and len(selectedElems) > 0: # 하나 이상인 경우
            return '\n'.join([elem.get_text() for elem in selectedElems]) # 각 요소의 text 뽑고, 그 요소 사이사이에 '\n'을 넣어 하나의 큰 문자열로 만듦
        return '' # 아무것도 못 찾은 경우

    def parse(self, url):
        bs = self.getPage(url) # 새로운 url에 해당하는 getPage( ) 메소드
        if bs is not None: # bs 잘 받아왔으면
            title = self.safeGet(bs, self.site.titleTag) # safeGet( ) 메소드
            body = self.safeGet(bs, self.site.bodyTag) # safeGet( ) 메소드
            if title != '' and body != '': # title, body 둘다 잘 가져왔을 때만
                content = Content(url, title, body)
                content.print() # 출력

    def crawl(self):
        """
        Get pages from website home page
        """
        bs = self.getPage(self.site.url) # 도메인주소에 해당하는 getPage( ) 메소드
        targetPages = bs.findAll('a', href=re.compile(self.site.targetPattern)) # 현재 html에서 href가 targetPattern인 a태그 모두 찾기
        for targetPage in targetPages: # targetPage(a태그들) 하나씩
            targetPage = targetPage.attrs['href'] # targetPage에 a태그 대신 href 속성의 value값 넣어줌
            if targetPage not in self.visited: # 방문한 적 없으면
                self.visited.append(targetPage) # 방문기록 history에 넣어줌
                if not self.site.absoluteUrl: # 절대주소가 아니라면 (지금 모두 /article/로 시작하는 상대주소인 상황)
                    targetPage = '{}{}'.format(self.site.url, targetPage) # 절대주소로 바꿈
                self.parse(targetPage) # parse( ) 메소드


reuters = Website('Reuters', 'https://www.reuters.com', '^(/article/)', False, 'h1', 'div.StandardArticleBody_body_1gnLA') # Website 객체
crawler = Crawler(reuters) # reuters 를 크롤링하기 위한 Crawler 객체
crawler.crawl()