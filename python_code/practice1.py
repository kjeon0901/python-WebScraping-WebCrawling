import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import time

#### BeautifulSoup, Selenium 같이 사용
#### [네이버 뉴스] - 7분야 각각의 탭에서 카테고리 + url(상대경로도 모두 절대경로로) + 5가지 요약문 + 각각의 기사입력 날짜데이터 출력

url = 'https://naver.com'
driver = webdriver.Chrome('C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe')
driver.get(url)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div[1]/ul[2]/li[2]/a').click()
bs = BeautifulSoup(driver.page_source)
var = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'} # 우회하기 위함

for idx, category in enumerate(bs.find_all('div', {'class':'main_component droppable'})):
    print("\n======",category.h4.get_text(), "======")
    for idx2, title in enumerate(category.find('ul').find_all('li')):
        if idx==0:
            print(title.a.get_text())
            urlpath = driver.current_url + title.a.get("href")
        else:
            print(title.a.strong.get_text())
            urlpath = title.a.get("href")
        print(urlpath)
        
        html = requests.get(urlpath, headers = var) # var에 담긴 fake user-agent 정보를 headers로 넣어줌. 
        bs2 = BeautifulSoup(html.text)
        print(bs2.find('span', {'class':'t11'}).get_text())
        time.sleep(0.5)
        
#driver.quit()
