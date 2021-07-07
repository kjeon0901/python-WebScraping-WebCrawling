from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql # 파이썬과 DB를 연결시켜주는 패키지
import csv # 파이썬과 csv를 연결시켜주는 패키지
from random import shuffle

# quiz 1. pages 테이블 안에 해당 페이지의 본문 or 제목(본문이 없는 경우)을 담은 content라는 컬럼 추가
# quiz 2. url 정보를 csv 파일에도 (mysql과 동시에) 저장하기

conn = pymysql.connect(host='127.0.0.1',
                       user='root', passwd='KJEON0901Q1W2E3R4', db='mysql', charset='utf8')
cur = conn.cursor() 
cur.execute('USE wikipedia')
cnt = 10

def insertPageIfNotExists(url):
    global cnt
    cur.execute('SELECT * FROM pages WHERE url = %s', (url)) # pages 테이블에서 해당 url을 가진 모든 row 가져옴
    if cur.rowcount == 0: # 하나도 없으면
        cnt = cnt-1
        if cnt < 0:
            return -1 # 10개의 url 저장되면 종료
        
        #### quiz 1 ####
        html = urlopen('http://en.wikipedia.org{}'.format(url))
        bs = BeautifulSoup(html, 'html.parser')
        content = bs.find('div', {'class': 'mw-parser-output'}).find('p', {'class': None})
        if content==None:
            content = bs.find('h1')
        cur.execute('INSERT INTO pages (url, content) VALUES (%s, %s)', (url, content.get_text())) # pages 테이블에 해당 url, content을 가진 새로운 row 추가
        ################
        
        conn.commit() 
        test = cur.lastrowid
        print('lastrowid:', test) 
        return test 
    else: # 있으면
        test1 = cur.fetchone()[0]
        print('fetchone()[0]:', test1) 
        return test1 
    
def loadPages():
    cur.execute('SELECT * FROM pages')
    pages = [row[1] for row in cur.fetchall()] # pages에 담긴 모든 row에 대해 url 가져와서 리스트에 담음
    return pages

def insertLink(fromPageId, toPageId):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s', 
                  (int(fromPageId), int(toPageId))) 
    if cur.rowcount == 0: # 하나도 없으면
        cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)', 
                    (int(fromPageId), int(toPageId)))
        conn.commit()
def pageHasLinks(pageId):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s', (int(pageId))) 
    rowcount = cur.rowcount
    if rowcount == 0: # 하나도 없으면
        return False
    return True # 하나라도 있으면

def getLinks(pageUrl, recursionLevel, pages): 
    pageId = insertPageIfNotExists(pageUrl) 
    if recursionLevel > 4 or pageId == -1:
        return
    
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser') 
    links = bs.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    links = [link.attrs['href'] for link in links] 

    for link in links: # link(href 속성값) 하나씩
        linkId = insertPageIfNotExists(link) 
        if linkId == -1:
            return
        insertLink(pageId, linkId) 
        if not pageHasLinks(linkId): 
            print("PAGE HAS NO LINKS: {}".format(link))
            pages.append(link) 
            getLinks(link, recursionLevel+1, pages) 
        
getLinks('/wiki/Kevin_Bacon', 0, loadPages()) # 처음엔 loadPages() : []
'''
lastrowid: 1
lastrowid: 2
PAGE HAS NO LINKS: /wiki/Kevin_Bacon_(disambiguation)
fetchone()[0]: 2
fetchone()[0]: 1
lastrowid: 3
PAGE HAS NO LINKS: /wiki/Kevin_Bacon_(producer)
fetchone()[0]: 3
lastrowid: 4
PAGE HAS NO LINKS: /wiki/Rotherham
fetchone()[0]: 4
lastrowid: 5
PAGE HAS NO LINKS: /wiki/Rotherham_(disambiguation)
fetchone()[0]: 5
fetchone()[0]: 4
lastrowid: 6
PAGE HAS NO LINKS: /wiki/Rotherham_(UK_Parliament_constituency)
fetchone()[0]: 6
lastrowid: 7
PAGE HAS NO LINKS: /wiki/Metropolitan_Borough_of_Rotherham
fetchone()[0]: 7
lastrowid: 8
PAGE HAS NO LINKS: /wiki/Rotherham,_New_Zealand
fetchone()[0]: 8
lastrowid: 9
PAGE HAS NO LINKS: /wiki/Alan_Rotherham
fetchone()[0]: 9
lastrowid: 10
PAGE HAS NO LINKS: /wiki/Arthur_Rotherham
fetchone()[0]: 10
'''

#### quiz 2 ####
final_urls = loadPages() # 프로그램 다시 실행하면 MySQL pages 테이블에 다음 row 10개 추가되는 것처럼, 얘도 다음 url 10개 추가됨. MySQL과 CSV에 같은 데이터가 저장됨. 
csvFile = open('pages_url.csv', 'w+', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    writer.writerow(['URL'])
    for url in final_urls:
        writer.writerow([url])
finally:
    csvFile.close()
################

cur.close()
conn.close()