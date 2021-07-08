from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql
from random import shuffle
import csv


conn = pymysql.connect(host='127.0.0.1',
                       user='root', passwd='!!!!!!!!', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')

test33 = []
def insertPageIfNotExists(url):
    global test33
    cur.execute('SELECT * FROM pages WHERE url = %s', (url))
    
    print("==================================================")
    html = urlopen('http://en.wikipedia.org{}'.format(url))
    bs = BeautifulSoup(html, 'html.parser')
        
    if cur.rowcount == 0:
        print(url)
       
        temp = bs.find('div',{'class':'mw-parser-output'}).find('p',{'class':None}).get_text()
        print(temp)
        
        csvFile = open('pages.csv', 'a', newline='', encoding='UTF-8')
        writer = csv.writer(csvFile)
        try:
            writer.writerow([url, temp])
        finally:
            csvFile.close()   
        
        #ALTER TABLE pages ADD content TEXT;  새로운 field를 하나 추가하여야한다.
        cur.execute('INSERT INTO pages (url,content) VALUES (%s, %s)', (url, temp))
        #cur.execute('INSERT INTO pages (url) VALUES (%s)', (url))
        conn.commit()
        print('lastrow_id : ', cur.lastrowid)
        return bs, cur.lastrowid
    else:
        test = cur.fetchone()[0]
        print('fetch_Id :', test)
        return bs, test

def loadPages():
    cur.execute('SELECT * FROM pages')
    pages = [row for row in cur.fetchall()]
    pages = list(pages)
    
    csvFile = open('pages.csv', 'wt+',  newline='', encoding='UTF-8')
    writer = csv.writer(csvFile)
    
    try:
        for row in pages:
            #writerow에 인풋값으로 들어오는 element 단위로 각각의 셀에 저장 된다. 
            #즉 바로 string이 들어오면 문자별로 셀에 저장된다
            writer.writerow([row[1], row[3]]) 
    finally:
            csvFile.close()
    
    pages_url = []   
    for row in pages:
        pages_url.append(row[1])
    
    return pages_url

def insertLink(fromPageId, toPageId):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s', 
                  (int(fromPageId), int(toPageId)))
    if cur.rowcount != 0:
        print('rowcount : {}, fromPageId:{}, toPageId:{} '.format(cur.rowcount, fromPageId , toPageId ))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)', 
                    (int(fromPageId), int(toPageId)))
        conn.commit()
def pageHasLinks(pageId):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s', (int(pageId)))
    rowcount = cur.rowcount
    if rowcount == 0:
        return False
    return True

def getLinks(pageUrl, recursionLevel, pages):
    #print('recursionLevel : {}'.format(recursionLevel))
    if recursionLevel > 4:
        return

    bs, pageId = insertPageIfNotExists(pageUrl)
    links = bs.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    links = [link.attrs['href'] for link in links]

    for link in links:
        bs, linkId = insertPageIfNotExists(link)
        insertLink(pageId, linkId)
        if not pageHasLinks(linkId):
            #print("PAGE HAS NO LINKS: {}".format(link))
            pages.append(link)
            print('link : ', link)
            getLinks(link, recursionLevel+1, pages)
        else:
            print('i,m here and fromPageId:{}, toPageId:{} '.format(linkId , pageId ))        


loded_text = loadPages()
getLinks('/wiki/Kevin_Bacon', 0, loded_text) 
cur.close()
conn.close()











