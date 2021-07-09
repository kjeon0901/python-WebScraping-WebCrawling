from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.support.ui import Select # 추가 안해주면 webdriver.support.ui.Select 이렇게 접근해야 함. 
from bs4 import BeautifulSoup
import time

url = "https://stat.kita.net/main.screen"
driver = webdriver.Chrome('C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe')
driver.get(url)

driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/ul/li[1]/a").click()
driver.find_element_by_link_text("품목 수출입").click()

# 100개씩 보기 + 조회 클릭
select = Select(driver.find_element_by_id('listCount'))
select.select_by_value('100')
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/fieldset/div[3]/a").click()

# 페이지 1 ~ 53(마지막)까지 이동
'''
url = driver.current_url
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
'''
bs = BeautifulSoup(driver.page_source) 
time.sleep(3)

#driver.find_element_by_xpath("//li[@class='on']/following-sibling::li").click()
var = '/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/span/a[{}]'
cnt = 0
       

while True:
    while True:
        cnt += 1
        next_page = var.format(cnt%10)
        try:
            driver.find_element_by_xpath(next_page).click()
            time.sleep(2)
        except:
            break
    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/a[2]').click()
        time.sleep(2)
    except:
        break
    

