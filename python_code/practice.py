from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

######### 문제 1. 재귀횟수 10번 (처음 실행까지 11번) 되면 프로그램 종료가 되는 코드 추가하라. 
'''
    # 재귀함수가 for문 안에 있기 때문에, 계속 for문의 첫 번째 loop만 만난다. 
    # 그러다가 a태그가 없어서 for문으로 들어오지 않고 이 getLinks함수가 종료되면, 
    # 이 함수가 호출된 곳으로 돌아가서 첫 번째 loop 끝나고 두 번째 loop로 넘어가게 된다. 
    # ex_
    #   getLinks()
    #       for-1
    #           getLinks()
    #               for-1
    #                   getLinks()
    #               for-2
    #                   getLinks()
    #                       for-1
    #                           getLinks()
    #       for-2
    #   ...
'''



'''
# 풀이 1. 

import sys

pages = set()
recursion = 10
def getLinks(pageUrl):
    global pages
    global recursion
    if recursion==-1:
        sys.exit("종료")
    if recursion <10:
        print("=============== 재귀", 10-recursion, "===============")

    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0]) # 가장 상위에 있는 문단 찾음. 
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href']) # 여기서 계속 except문으로 빠짐. 
        # 이렇게 find.find.find... 면 무.조.건. AttributeError 예외처리 필요!!
        # None을 받아오는 것까지는 Okay인데, None.find 가 되면 AttributeError!
        
    except AttributeError:
        print('This page is missing something! Continuing.')
    
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                recursion-=1
                getLinks(newPage) # 재귀함수

getLinks('') 
'''


# 풀이 2. --good

pages = set()
recursion = 10
def getLinks(pageUrl):
    global pages
    global recursion
    if recursion==-1:
        return
    if recursion <10:
        print("=============== 재귀", 10-recursion, "===============")

    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
        
    except AttributeError:
        print('This page is missing something! Continuing.')
    
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                recursion-=1
                return getLinks(newPage) # 재귀함수. 
                # 여기서 return 안해주면 재귀 11만 넘어가고 재귀 12부터 또 이어서 하게 됨. 
    # for문 안 들어갔을 때, 여기서 이번 getLinks()함수는 아무 return 없이 그냥 끝나버림
            
getLinks('')


