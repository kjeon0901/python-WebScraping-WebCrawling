from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os, sys
import shutil

url = ('https://stat.kita.net/main.screen')

defalt_next_page_tag_path = "/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/span/"

work_place_root_default_path = 'C:/Users/HS-802/Google Drive/sync folder all/회사업무 외 작업폴더'
work_place_root_down_path = 'C:/Users/HS-802/Downloads'

driver = webdriver.Chrome('C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe')
driver.get(url)

#먼저 국내통계를 클릭해야 그 하위 카테고리가 생기고 그안에 우리가 들어가고자 목적하는 품목수출입 링크가 존재한다.
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/ul/li[1]/a/img").click()
driver.find_element_by_link_text("품목 수출입").click()

#100개씩 보기 선택 
select = Select(driver.find_element_by_id('listCount'))
select.select_by_value('100')

#년월에서 1월 선택
select = Select(driver.find_element_by_name('s_month'))
select.select_by_value('01')

#조회 클릭 하여서 100개씩 보기와 월정보 갱신 
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/fieldset/div[3]").click()
time.sleep(1)

bs = BeautifulSoup(driver.page_source)

page_link = bs.find('div', id='pageArea').find('span').find_all('a')
page_link_count = len(page_link)


'''def download(driver, bs): # 파일다운 + 이동 + 이름변경해서 폴더 안에 저장
        
    shutil.move(path+'/K-stat 총괄 .xls', path+'/fileDir') # path + '/K-stat 총괄 .xls' 이 경로의 파일을 path+'/fileDir' 이 경로의 해당 폴더 안으로 이동시켜주세요
    os.rename(path+'/fileDir/K-stat 총괄 .xls', path+'/fileDir/K-stat file_'+num+'.xls')
  '''  
def next_page_method(page_link_in_fnc_count_input):
    link_list = []
    
    #download(driver, bs)
    for row in range(1, page_link_in_fnc_count_input+1):
        driver.find_element_by_xpath(defalt_next_page_tag_path + 'a['+str(row)+']' ).click()
        time.sleep(1)
        print(row)
        bs = BeautifulSoup(driver.page_source)
        #download(driver, bs)
        
    last_page_num = driver.find_element_by_xpath(defalt_next_page_tag_path+'strong').text
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/a[2]").click()
    time.sleep(1)
    
    bs = BeautifulSoup(driver.page_source)
    page_link_in_fnc_output = bs.find('div', id='pageArea').find('span').find_all('a')
    page_link_in_fnc_output_count = len(page_link_in_fnc_output)
    next_page_num = driver.find_element_by_xpath(defalt_next_page_tag_path + 'strong').text

    return last_page_num, next_page_num, page_link_in_fnc_output_count

page_num_main= next_page_method(page_link_count)
    
while (page_num_main[0] != page_num_main[1] ):
    print(page_num_main[0], page_num_main[1])
    page_num_main = next_page_method(page_num_main[2])


