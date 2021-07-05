from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql
from random import shuffle

conn = pymysql.connect(host='127.0.0.1',
                       user='root', passwd='KJEON0901Q1W2E3R4', db='mysql', charset='utf8')
cur = conn.cursor() # sql문을 실행시키고 결과를 얻어올 때 사용할 커서(cursor) 만듦
cur.execute('USE wikipedia') # sql문을 실행(execute)

def insertPageIfNotExists(url):
    cur.execute('SELECT * FROM pages WHERE url = %s', (url)) # pages 테이블에서 해당 url을 가진 모든 row 가져옴
    if cur.rowcount == 0: # 하나도 없으면
        cur.execute('INSERT INTO pages (url) VALUES (%s)', (url)) # pages 테이블에 해당 url을 가진 새로운 추가
        conn.commit()
        return cur.lastrowid # db_cursor를 이용해 excute한 테이블의 마지막 행 id 값을 가져옴
    else: # 있으면
        return cur.fetchone()[0] # 한 줄 row을 읽어서 0번째 column값을 리턴 -> id 리턴

def loadPages():
    cur.execute('SELECT * FROM pages')
    pages = [row[1] for row in cur.fetchall()]
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

def getLinks(pageUrl, recursionLevel, pages): # pageUrl : 현재 웹페이지 주소
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
        if not pageHasLinks(linkId): # links 테이블에 linkId를 fromPageId로 갖는 row가 하나도 없다면
            print("PAGE HAS NO LINKS: {}".format(link))
            pages.append(link) # pages 테이블에 link를 url로 갖는 새로운 row 추가
            return getLinks(link, recursionLevel+1, pages) # 재귀→계속 첫 번째 내부링크로만 들어감
        
        
getLinks('/wiki/Kevin_Bacon', 0, loadPages()) 
cur.close()
conn.close()