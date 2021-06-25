import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import time

#### BeautifulSoup, Selenium 같이 사용
#### [네이버 뉴스] - 7분야 각각의 탭에서 카테고리 + url(상대경로도 모두 절대경로로) + 5가지 요약문 + 각각의 기사입력 날짜데이터 출력
'''
<<< 각각의 기사입력 날짜데이터 출력 >>>
웹브라우저를 거치지 않고 파이썬으로 urlopen 이라는 request를 통해 직접 html을 가져오는 게 훨씬 빠름.
근데, 웹브라우저로 접근하면 접근 가능하고, 파이썬으로 접근하면 접근 에러 뜸. 
    => 네이버에서 브라우저로 접근하는 것 vs. 파이썬으로 접근하는 것 구분짓는 어떤 걸 가지고 있구나!
    => 얘를 속여서 fake로 우회하는 방법이 필요하겠군!!
    

'''

url = 'https://naver.com'
driver = webdriver.Chrome('C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe')
driver.get(url)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div[1]/ul[2]/li[2]/a').click()

bs = BeautifulSoup(driver.page_source)

for idx, category in enumerate(bs.find_all('div', {'class':'main_component droppable'})):
    print("\n======",category.h4.get_text(), "======")
    for idx2, title in enumerate(category.find('ul').find_all('li')):
        '''
        1. children 쓰면 보이지 않는 잡다한 애들까지 다 잡히는 경우 多   →   find_all('li') 처럼 태그를 딱 지칭해주는 게 BETTER
        2. 이 부분에선 사실 'ul'태그가 하나씩밖에 없음   →   여기선 굳이 {'class':{'hdline_article_list', 'mlist2 no_bg'}} 이렇게 특정하지 않아도 됨. 
        '''
        if idx==0:
            print(title.a.get_text())
            urlpath = driver.current_url + title.a.get("href")
        else:
            print(title.a.strong.get_text())
            urlpath = title.a.get("href")
        print(urlpath)
        
        html = urlopen(urlpath)
        bs2 = BeautifulSoup(html.read(), 'html.parser')
        print(bs2.find('span', {'class':'t11'}).get_text())
        # RemoteDisconnected: Remote end closed connection without response 접근 에러 뜸
        
#driver.quit()
