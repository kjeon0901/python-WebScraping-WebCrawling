from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://pjt3591oo.github.io'

start = time.time()

driver = webdriver.Chrome('chromedriver')
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

soup1 = soup.select('div')
soup2 = soup.select('div')
soup3 = soup.select('div')
soup4 = soup.select('div')
soup5 = soup.select('div')

end = time.time() - start

print(end)
