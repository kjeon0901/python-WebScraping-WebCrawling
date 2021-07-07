from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql # 파이썬과 DB를 연결시켜주는 패키지
from random import shuffle

# quiz 1. pages 테이블 안에 해당 페이지의 본문 or 제목(본문이 없는 경우)을 담은 content라는 컬럼 추가

conn = pymysql.connect(host='127.0.0.1',
                       user='root', passwd='KJEON0901Q1W2E3R4', db='mysql', charset='utf8')
cur = conn.cursor() # sql문을 실행시키고 결과를 얻어올 때 사용할 커서(cursor) 만듦
cur.execute('USE wikipedia') # sql문을 실행(execute), execute : 파이썬에서 mysql로 쿼리문을 던져주는 함수

def insertPageIfNotExists(url):
    cur.execute('SELECT * FROM pages WHERE url = %s', (url)) # pages 테이블에서 해당 url을 가진 모든 row 가져옴
    if cur.rowcount == 0: # 하나도 없으면 (DB가 파이썬 변수 rowcount에 0을 담아줌)
        html = urlopen('http://en.wikipedia.org{}'.format(url))
        bs = BeautifulSoup(html, 'html.parser')
        content = bs.find('div', {'class': 'mw-parser-output'}).find('p', {'class': None}).get_text()
        if content==None:
            content = bs.find('h1').get_text()
        cur.execute('INSERT INTO pages (url, content) VALUES (%s, %s)', (url, content)) # pages 테이블에 해당 url을 가진 새로운 추가
        conn.commit() # 실제로 데이터베이스에 써줌
        test = cur.lastrowid
        print('lastrowid:', test) # 새로운 페이지에 들어올 때마다 실행되므로 1씩 증가되며 출력
        return test # db_cursor를 이용해 excute한 테이블의 마지막 row id 값을 가져옴 => 지금 if문 안에서는 무조건 0이 리턴됨
    else: # 있으면
        test1 = cur.fetchone()[0]
        print('fetchone()[0]:', test1) # 지금 excute한 url이 pages 테이블 상의 어떤 row에 존재하는지 출력 => 당연히 중복된 값 출력 가능
        return test1 # db_cursor를 이용해 excute한 쿼리문에 해당하는 한 줄의 row을 읽어서 0번째 column값을 리턴 -> id 리턴
                                 # 즉, MySQL 에 직접 SELECT * FROM pages WHERE url = .. 쿼리문을 입력하면 출력되는 row를 파이썬으로 가져옴
        '''
        cur.fetchall() : 모든 데이터를 한꺼번에 가져올 때 사용
        cur.fetchone() : 1개의 데이터를 가져올 때 사용. 
        cur.fetchmany(n) : n개 만큼의 데이터를 한꺼번에 가져올 때 사용
        
        연속으로 실행 시, 마지막으로 읽어들인 데이터의 다음 데이터를 자동으로 가져온다.
            ex_  5개 row가 있다면
            print(cur.fetchmany(2))
            print(cur.fetchone())
            print(cur.fetchall())
            --------------------------------------
            [(1, '/wiki/Kevin_Bacon', '2021-07-05 10:26:43'), (2, '/wiki/Kevin_Bacon_(disambiguation)', '2021-07-05 10:26:44')]
            (3, '/wiki/Kevin_Bacon_(producer)', '2021-07-05 10:26:45')
            [(4, '/wiki/Rotherham', '2021-07-05 10:26:46'), (5, '/wiki/Rotherham_(disambiguation)', '2021-07-05 10:26:47')]
        '''
def loadPages():
    cur.execute('SELECT * FROM pages')
    pages = [row[1] for row in cur.fetchall()] # pages에 담긴 모든 row에 대해 url 가져와서 리스트에 담음
    return pages

def insertLink(fromPageId, toPageId):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s', 
                  (int(fromPageId), int(toPageId))) # links 테이블에서 해당 fromPageId, toPageId를 가진 모든 row 가져옴
    if cur.rowcount == 0: # 하나도 없으면
        cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)', 
                    (int(fromPageId), int(toPageId))) # links 테이블에 해당 fromPageId, toPageId를 갖는 새로운 row 추가
        conn.commit()
def pageHasLinks(pageId):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s', (int(pageId))) # links 테이블에서 해당 pageId를 fromPageId로 가진 모든 row 가져옴
    rowcount = cur.rowcount
    if rowcount == 0: # 하나도 없으면
        return False
    return True # 하나라도 있으면

def getLinks(pageUrl, recursionLevel, pages): # pageUrl : 현재 웹페이지 주소, pages : pages 테이블에 담긴 모든 url 담은 리스트
    if recursionLevel > 4: # 재귀 5번 돌고 6번째 끝남. 
        return

    pageId = insertPageIfNotExists(pageUrl) # pages에서 pageUrl을 url로 가진 첫 번째 row에 담긴 id 가져옴
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser') # urlopen으로 열면 html만 넣어줘도 됨
    links = bs.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')) # html 안의 모든 내부링크 가진 a태그 찾아서 리턴
    links = [link.attrs['href'] for link in links] # href 속성값만 빼서 담음

    for link in links: # link(href 속성값) 하나씩
        linkId = insertPageIfNotExists(link) # pages 테이블에서 link를 url로 가진 첫 번째 row에 담긴 id 가져옴
        insertLink(pageId, linkId) # links 테이블에 pageId, linkId를 각각 fromPageId, toPageId로 갖는 row가 없다면 추가. 
                                   # pages 테이블에 담긴 페이지들 간의 연결관계를 links 테이블에 추가. 즉 어떤 페이지에서 어떤 페이지로 연결되고 있는지 페이지 id로 각각 나타냄. 
        if not pageHasLinks(linkId): # links 테이블에 linkId(toPageId)를 fromPageId로 갖는 row가 있을 때, 즉 이미 한 번 들려서 pageUrl이었던 적 있는 url을 다른 페이지의 내부 링크로 또 만날 때
                                     # 재귀로 인해 그 페이지로 다시 들어가서 무한 루프로 빠지면 안 되기 때문에 if문 못 들어오도록 걸러줌.
            print("PAGE HAS NO LINKS: {}".format(link))
            pages.append(link) # pages 테이블에 담긴 모든 url 담은 리스트에 link도 추가
            getLinks(link, recursionLevel+1, pages) # 재귀→계속 첫 번째 내부링크로만 들어감
        
        
getLinks('/wiki/Kevin_Bacon', 0, loadPages()) # 처음엔 loadPages() : []
'''
PAGE HAS NO LINKS: /wiki/Philadelphia,_Pennsylvania
PAGE HAS NO LINKS: /wiki/Philly_(disambiguation)
PAGE HAS NO LINKS: /wiki/Philadelphia
PAGE HAS NO LINKS: /wiki/Philadelphia_(disambiguation)
PAGE HAS NO LINKS: /wiki/Philadelphia_County,_Pennsylvania
'''
cur.close()
conn.close()