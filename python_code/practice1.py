## Crawling through sites with search

# Quiz. 전역변수 사용해서 print되는 text들을 전역변수에 담아보기. 

#ln [1] :

    
all_ = []

class Content:
    """Common base class for all articles/pages"""

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Flexible printing function controls output
        """
        print('New article found for topic: {}'.format(self.topic))
        print('URL: {}'.format(self.url))
        print('TITLE: {}'.format(self.title))
        print('BODY:\n{}'.format(self.body))
        
    def print_2(self):
        return self.topic, self.url, self.title, self.body


#ln [2] :

class Website:
    """Contains information about website structure"""

    def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name # 사이트이름
        self.url = url # 사이트 도메인주소
        self.searchUrl = searchUrl # 검색창url - 활용도Good!
        self.resultListing = resultListing # 검색 결과 나온 요소 위치 찾는 태그
        self.resultUrl = resultUrl # 각 요소의 제목(==링크) 위치 찾는 태그
        self.absoluteUrl = absoluteUrl # 절대주소 : True, 상대주소 : False
        self.titleTag = titleTag # 링크 내부 title 위치 찾는 태그
        self.bodyTag = bodyTag # 링크 내부 body 위치 찾는 태그


#ln [3] :

import requests
from bs4 import BeautifulSoup

class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''

    def search(self, topic, site):
        """
        Searches a given website for a given topic and records all pages found
        """
        bs = self.getPage(site.searchUrl + topic) # '검색창에 topic을 검색'한 url에 해당하는 html을 파싱하는 객체
        searchResults = bs.select(site.resultListing) # 검색 결과 검색된 모든 요소에 대한 태그 모두 찾아서 담음
        for result in searchResults:
            #try:
            url = result.select_one(site.resultUrl).attrs['href']
            # 혹시 하나의 기사 안에 같은 클래스인 여러 태그가 있을 수 있으니까 첫 번째 고름 (select만 하면 여러개 담겨서 attrs['href'] 접근 불가)
            # Check to see whether it's a relative or an absolute URL
            if(site.absoluteUrl): # 절대주소면
                bs = self.getPage(url) # 그대로
            else: # 상대주소면
                bs = self.getPage(site.url + url) # 도메인주소 뒤에 붙여 절대주소로 바꿈
            if bs is None:
                print('Something was wrong with that page or URL. Skipping!')
                return
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            #print('===============================================')
            #print(title, body)
            if title != '' and body != '': # O\'Reilly 여기서 안들어가짐!!!! => 해결o
                print('===============================================')
                content = Content(topic, title, body, url)
                content.print()
                all_.append(content.print_2()) # 하나로 받았으므로 튜플로 받아짐
            #except AttributeError as e:
            #    print(e)

crawler = Crawler()

siteData = [
    ['O\'Reilly Media', 'http://oreilly.com', 'https://ssearch.oreilly.com/?q=',
        'article.result', 'p.title a', True, 'p[itemprop=summary]', 'div[itemprop=description]'],
    ['Reuters', 'http://reuters.com', 'http://www.reuters.com/search/news?blob=', 'div.search-result-content',
        'h3.search-result-title a', False, 'h1', 'div.ArticleBodyWrapper, div.ArticleBody__content___2gQno2.paywall-article'],
    ['Brookings', 'http://www.brookings.edu', 'https://www.brookings.edu/search/?s=',
        'div.list-content article[class*=has-image]', 'h4.title a', True, 'h1.report-title', 'div.post-body.post-body-enhanced']
]
sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2],
                         row[3], row[4], row[5], row[6], row[7]))

topics = ['python', 'data science']
for topic in topics:
    print('GETTING INFO ABOUT: ' + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)