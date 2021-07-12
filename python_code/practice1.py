from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os, sys
import shutil
import pandas as pd


#셀레니움을 이용해서 클릭이라는 행위를 할때에 항상 유효하지않은 값이 담겨있을 가능성에 대한 예외처리를 추가해놔야한다. 
url = ('https://stat.kita.net/main.screen')

defalt_next_page_tag_path = "/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/span/"

'/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/span/a[9]'

#work_place_root_default_path = 'C:/Users/HS-802/Google Drive/sync folder all/회사업무 외 작업폴더'
#work_place_root_down_path = 'C:/Users/HS-802/Downloads'
work_place_root_default_path = 'E:/no1/cho/web_crawler/23_web_Scraping/fileDir/'
work_place_root_down_path = 'C:/Users/wheng/Downloads/'

#driver = webdriver.Chrome(work_place_root_default_path+'/23_web_Scraping/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome('E:/no1/cho/파이썬_머신러닝/chromedriver_win32/chromedriver.exe')

driver.get(url)

#먼저 국내통계를 클릭해야 그 하위 카테고리가 생기고 그안에 우리가 들어가고자 목적하는 품목수출입 링크가 존재한다.
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/ul/li[1]/a/img").click()
driver.find_element_by_link_text("품목 수출입").click()

#100개씩 보기 선택 
select = Select(driver.find_element_by_id('listCount'))
select.select_by_value('100')

#년월에서 1월 선택
#select = Select(driver.find_element_by_name('s_month'))
#select.select_by_value('01')

#조회 클릭 하여서 100개씩 보기와 월정보 갱신 
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/fieldset/div[3]").click()
time.sleep(3)

#페이지 소스를 bs를 통해서 읽어옴
#소스를 파싱하는것은 bs가 셀레니움을 이용하는것보다 더 빠르기 때문에 셀레니움은 최대한 클릭이나 선택등 필요한 용도로만 쓴다
bs = BeautifulSoup(driver.page_source)

#next페이지의 개수를 센다(최대 9페이지)
page_link = bs.find('div', id='pageArea').find('span').find_all('a')
page_link_count = len(page_link)

#페이지 장수만큼 다음페이지로 넘겨주기
#6단위 코드별로 수출 증감률을 누적적으로 더해준후 리스트에 저장 시키기

test2 = []
def click_down_button(): # 예외처리 - 재귀함수로 하면 코드 간단해짐!
    global test2
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/div[1]/div/a[1]").click()
    time.sleep(1)
    print('0')
    try:
        xls = pd.read_excel(work_place_root_down_path + 'K-stat 총괄 .xls')
        print('1')
        if xls.shape[0] < 10:
            print('file empty')
            os.remove(work_place_root_down_path + 'K-stat 총괄 .xls')
            time.sleep(1)
            click_down_button()
        else:
            test2.append(xls)
    except:
        print('2')
        time.sleep(1)
        os.remove(work_place_root_down_path + 'K-stat 총괄 .xls')
        time.sleep(1)
        click_down_button()
        
        

counter = 0
test = []
def next_page_method(page_link_in_fnc_count_input):
    global test
    global counter
    link_list = []
    #페이지 장수만큼 마지막 태그이름(a[1~9])을 만들어서 리스트에 담아놓는다.
    for row in range(1, page_link_in_fnc_count_input+1):
        #파일 다운로드
        #driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/div[1]/div/a[1]").click()
        click_down_button()
        time.sleep(1)
            
        #타겟 폴더로 방금 수집한 폴더를 이동    #2초를 기다렸음에도 아직 다운이 되지 않아서 파일이 없다는 에러 발생가능 예외처리 필수
        shutil.move(work_place_root_down_path +'/K-stat 총괄 .xls', work_place_root_default_path)
        #변경될 파일 이름
        file_name = 'kstat_' + str(counter) + '.xls'
        counter = counter + 1
        #이름 변경
        os.rename(work_place_root_default_path + 'K-stat 총괄 .xls', work_place_root_default_path + file_name)
        
        #다음 웹페이지 이동
        driver.find_element_by_xpath(defalt_next_page_tag_path + "a["+str(row)+']').click()
        #페이지 이동후 다운로드 버튼을 누르기 전에 잠시 대기하지 않으면 empty 파일이 다운로드 된다.
        time.sleep(0.5)
        #print(row)
        bs = BeautifulSoup(driver.page_source)
    
    click_down_button()
    #타겟 폴더로 방금 수집한 폴더를 이동
    shutil.move(work_place_root_down_path +'/K-stat 총괄 .xls', work_place_root_default_path)
    #변경될 파일 이름
    file_name = 'kstat_' + str(counter) + '.xls'
    counter = counter + 1
    #이름 변경
    os.rename(work_place_root_default_path + 'K-stat 총괄 .xls', work_place_root_default_path + file_name)
        
    #마지막 웹페이지 인지 판단하기 위해서 마지막 페이지 링크의 text를 저장(53페이지가 있는 웹페이지는 다음 웹페이지 목록 이동을 클릭해도 여전히 같은 페이지에 위치한다.)
    last_page_num = driver.find_element_by_xpath(defalt_next_page_tag_path+'strong').text
    print('last_page_num :', last_page_num)
    
    #다음 페이지 목록으로 이동 클릭 #다음페이지로 이동하기도 전에 페이지 소스를 읽어버리는 이슈
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/a[2]").click()
    time.sleep(3)  
    
    #다음 페이지 목록으로 이동 후 해당 목록에 페이지 장수가 몇개가 있는지 카운트 하기
    bs = BeautifulSoup(driver.page_source)
    page_link_in_fnc_output = bs.find('div', id='pageArea').find('span').find_all('a')
    page_link_in_fnc_output_count = len(page_link_in_fnc_output)
    next_page_num = driver.find_element_by_xpath(defalt_next_page_tag_path + 'strong').text
    print('next_page :', next_page_num)

    #이동전 페이지 목록의 마지막 페이지 text, 이동후 페이지 목록의 첫번째 페이지 text, 이동후 페이지 카운트 갯수 리턴
    return last_page_num, next_page_num, page_link_in_fnc_output_count

page_num_main= next_page_method(page_link_count)
    
while (page_num_main[0] != page_num_main[1] ):
    #print(page_num_main[0], page_num_main[1])
    page_num_main = next_page_method(page_num_main[2])
