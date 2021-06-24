from bs4 import BeautifulSoup
from selenium import webdriver
import time

#### 네이버 뉴스 - 7분야 각각의 탭에서 탭 + 5가지 요약문 출력  (BeautifulSoup, Selenium 같이 사용)

url = 'https://naver.com'
driver = webdriver.Chrome('C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe')
driver.get(url)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a').click()
bs = BeautifulSoup(driver.page_source)

for idx, category in enumerate(bs.find_all('div', {'class':'main_component droppable'})):
    print("\n======",category.find('div', {'class':'com_header'}).h4.get_text(), "======")
    for title in category.find('ul', {'class':{'hdline_article_list', 'mlist2 no_bg'}}).find_all('li'):
        if idx==0:
            print(title.a.get_text())
        else:
            print(title.a.strong.get_text())

driver.quit()