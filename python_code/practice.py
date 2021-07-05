from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql # 파이썬과 MySQL 연동 => 서로 데이터 주고받을 수 있음. 
import re

conn = pymysql.connect(host='127.0.0.1',
                       user='root', passwd='!!!!!!!!', db='mysql', charset='utf8') # passwd에 내 mysql 비밀번호 넣기
cur = conn.cursor() # 파이썬에서 긁어온 데이터를 MySQL 데이터베이스로 넘겨주기 위한 객체
cur.execute('USE scraping') # USE scraping : mysql에서 쓰는 쿼리문. scraping 사용하기 위해 mysql로 들어가는 쿼리문. 

random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute('INSERT INTO pages (title, content) VALUES ("%s", "%s")', (title, content)) # 이 부분은 cowork에서 다른 팀원들이 코드 어떻게 짜든 상관 없는 부분 (github의 add같은 느낌..?)
        # INSERT INTO pages (title, content) VALUES ("%s", "%s") : mysql 쿼리문. => pages 테이블의 title, content 컬럼에다가 각각 해당 %s값을 넣어주겠다. 
    cur.connection.commit() # 실제로 데이터베이스에 써넣는 행위 (github commit과 같은 개념으로 log가 계속 누적됨.)

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org'+articleUrl)
    bs = BeautifulSoup(html, 'html.parser') # urlopen으로 불러오면 html만 넣어줘도 됨
    title = bs.find('h1').get_text()
    content = bs.find('div', {'id':'mw-content-text'}).find('p').get_text()
    store(title, content)
    return bs.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')) # html 안의 모든 내부링크 찾아서 리턴

links = getLinks('/wiki/Kevin_Bacon')
try:
    while len(links) > 0: # 랜덤으로 들어간 어떤 웹페이지가 내부 링크를 갖지 않을 때까지
         newArticle = links[random.randint(0, len(links)-1)].attrs['href'] # 전체 a태그 중 균일분포 랜덤으로 하나 뽑고 href 속성값(링크) 담음
         print(newArticle) # 뽑은 링크 출력
         links = getLinks(newArticle) # 이 코드를 통해 계속 내부링크로 타고 들어감
finally:
    cur.close()
    conn.close()