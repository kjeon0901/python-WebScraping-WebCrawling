from bs4 import BeautifulSoup
from selenium import webdriver
import time

#### BeautifulSoup, Selenium 같이 사용하여, 네이버 사전 자동으로 열어 태그 text 긁어오기

# Selenium 객체 driver로 페이지 클릭해 접속하기
driver = webdriver.Chrome('C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe')
url = 'https://www.naver.com'
driver.get(url)

# 네이버에서 사전 클릭하여 네이버 사전 페이지로 접속하기
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[1]/a').click()

# BeurifulSoup 객체 bs로 html 파싱해서 원하는 text 가져오기
bs = BeautifulSoup(driver.page_source) # 여기서 html 넣어줘야 하므로 (html == driver.page_source)

temp = bs.find('div', {'id':'content'}).find_all('h2')
for var in temp:
    print(var.get_text())

time.sleep(1)
driver.quit()
