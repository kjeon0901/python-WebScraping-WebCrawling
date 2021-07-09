from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.support.ui import Select # 추가 안해주면 webdriver.support.ui.Select 이렇게 접근해야 함. 
from bs4 import BeautifulSoup
import time
import shutil
import os, sys
import csv
import pandas as pd

url = "https://stat.kita.net/main.screen"
driver = webdriver.Chrome('C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe')
driver.get(url)

driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/ul/li[1]/a").click()
driver.find_element_by_link_text("품목 수출입").click()
time.sleep(1)

# 100개씩 보기 + 조회 클릭
select = Select(driver.find_element_by_id('listCount'))
select.select_by_value('100')
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/fieldset/div[3]/a").click()
time.sleep(1)

# 페이지 1 ~ 53(마지막)까지 이동, 전체 데이터 전처리 후 다운받기(다운 일단 받고, 비어있는 데이터가 있으면 다시 다운받도록)
# 데이터 옮

'''
def filedown(): # 파일다운 + 이동 + 이름변경해서 폴더 안에 저장
    bs = BeautifulSoup(driver.page_source) 
    while True:
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/form/div[1]/div/a[1]').click()
        time.sleep(1)
    
        data = pd.read_excel(io='C:/Users/hs-702/Downloads/K-stat 총괄 .xls') #이 경로의 파일을 열고 불러와 객체로 f에 담기 (더블클릭 따닥-!)
        if data.isna().sum() == 0:
            print('null값 없음')
            break
    num = bs.find('strong', {'class':'selected'}).get_text()
    shutil.move('C:/Users/hs-702/Downloads'+'/K-stat 총괄 .xls', 'C:/Users/hs-702/Desktop/kjeon/python_code'+'/Kstat_FileDir') # path + '/K-stat 총괄 .xls' 이 경로의 파일을 path+'/fileDir' 이 경로의 해당 폴더 안으로 이동시켜주세요
    os.rename('C:/Users/hs-702/Desktop/kjeon/python_code'+'/Kstat_FileDir/K-stat 총괄 .xls', 'C:/Users/hs-702/Desktop/kjeon/python_code'+'/Kstat_FileDir/K-stat file_'+num+'.xls')
'''


driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/form/div[1]/div/a[1]').click()
time.sleep(1)
bs = BeautifulSoup(driver.page_source) 

last_1stPage = bs.find('strong', {'class':'selected'}).get_text()

num = bs.find('strong', {'class':'selected'}).get_text()
print("num", num)
shutil.move('C:/Users/hs-702/Downloads'+'/K-stat 총괄 .xls', 'C:/Users/hs-702/Desktop/kjeon/python_code'+'/Kstat_FileDir') # path + '/K-stat 총괄 .xls' 이 경로의 파일을 path+'/fileDir' 이 경로의 해당 폴더 안으로 이동시켜주세요
os.rename('C:/Users/hs-702/Desktop/kjeon/python_code/Kstat_FileDir'+'/K-stat 총괄 .xls', 'C:/Users/hs-702/Desktop/kjeon/python_code/Kstat_FileDir'+'/K-stat file_'+num+'.xls')

while True:
    try:
        driver.find_element_by_xpath("//strong[@class='selected']/following-sibling::a[1]").click()
    except:
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/a[2]").click()
        bs = BeautifulSoup(driver.page_source) 
        if bs.find('strong', {'class':'selected'}).get_text() == last_1stPage: 
            # 여기서 프로그램 종료 안 되고 에러나면서 끝남. 해결 필요!
            break
        else:
            last_1stPage = bs.find('strong', {'class':'selected'}).get_text()
    time.sleep(5)
    
    # 파일다운 + 이동 + 이름변경해서 폴더 안에 저장
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/form/div[1]/div/a[1]').click()
    time.sleep(1)
    bs = BeautifulSoup(driver.page_source) 

    num = bs.find('strong', {'class':'selected'}).get_text()
    print("num", num)
    shutil.move('C:/Users/hs-702/Downloads'+'/K-stat 총괄 .xls', 'C:/Users/hs-702/Desktop/kjeon/python_code'+'/Kstat_FileDir') # path + '/K-stat 총괄 .xls' 이 경로의 파일을 path+'/fileDir' 이 경로의 해당 폴더 안으로 이동시켜주세요
    os.rename('C:/Users/hs-702/Desktop/kjeon/python_code/Kstat_FileDir'+'/K-stat 총괄 .xls', 'C:/Users/hs-702/Desktop/kjeon/python_code/Kstat_FileDir'+'/K-stat file_'+num+'.xls')

    









'''
var = '/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/span/a[{}]'
cnt = 0
while True:
    cnt += 1
    print(cnt)
    if cnt % 10 == 0:
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/a[2]').click()
        time.sleep(2)
        #download()
        continue
    next_page = var.format(cnt%10)
    try:
        driver.find_element_by_xpath(next_page).click()
    except:
        break
    time.sleep(2)


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
'''

'''
#driver.find_element_by_xpath(var+str(now)+']').click()
#now = bs.find('strong', class_='selected').get_text()
#driver.find_element_by_link_text(now+1).click()
#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/span/strong").click()
#/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/span/strong
#/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/span/a[1]

try:
    driver.find_element_by_xpath("//strong[@class='selected']/following-sibling::a").click()
except:
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/a[2]").click()
'''
