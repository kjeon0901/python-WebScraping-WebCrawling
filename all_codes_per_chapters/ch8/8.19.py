# selenium 사용시간 측정
from selenium import webdriver
import time

url = 'https://pjt3591oo.github.io'

selenium_start = time.time()

driver = webdriver.Chrome('chromedriver')
driver.get(url)

div_selectors11 = driver.find_elements_by_css_selector('div')
div_selectors12 = driver.find_elements_by_css_selector('div')
div_selectors13 = driver.find_elements_by_css_selector('div')
div_selectors14 = driver.find_elements_by_css_selector('div')
div_selectors15 = driver.find_elements_by_css_selector('div')

selenium_end = time.time() - selenium_start

print('usage selenium  : %f' %(selenium_end))

# bs4 사용시간 측정
import requests as rq
from bs4 import BeautifulSoup

bs4_start = time.time()

res = rq.get(url)
soup = BeautifulSoup(res.content, 'lxml')
div_selectors21 = soup.select('div')
div_selectors22 = soup.select('div')
div_selectors23 = soup.select('div')
div_selectors24 = soup.select('div')
div_selectors25 = soup.select('div')

bs4_end = time.time() - bs4_start

print('usage bs4  : %f' %(bs4_end))
