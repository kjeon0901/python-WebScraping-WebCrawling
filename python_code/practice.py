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
driver = webdriver.Chrome('C:/Users/hs703/Desktop/kjeon/chromedriver_win32/chromedriver.exe')
#driver = webdriver.Chrome('C:/Users/kjeon0901/Desktop/21proj/study/python-WebScraping-WebCrawling/chromedriver_win32/chromedriver.exe')
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
# 예외처리 1. 비어있는 데이터 다운받은 경우
# 예외처리 2. 없는 데이터를 shutil.move()하려고 하는 경우
# concat 로 폴더에 저장된 모든 excel 파일을 하나의 excel 파일로 취합. 

for _ in range(5):
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/a[2]").click()
    time.sleep(5)
    bs = BeautifulSoup(driver.page_source) 
    last_1stPage = bs.find('strong', {'class':'selected'}).get_text()
    print(last_1stPage)


bs = BeautifulSoup(driver.page_source) 
last_1stPage = bs.find('strong', {'class':'selected'}).get_text()
num = bs.find('strong', {'class':'selected'}).get_text()
while True:
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/form/div[1]/div/a[1]').click()
    time.sleep(3)
    data = pd.read_excel('C:/Users/hs703/Downloads/K-stat 총괄 .xls') #이 경로의 파일을 열고 불러와 객체로 f에 담기 (더블클릭 따닥-!)
    if data.shape[0] >= 103 and data.shape[1] >= 13:
        print('num', num, '성공')
        break
    print('num', num, '실패')
    os.remove('C:/Users/hs703/Downloads/K-stat 총괄 .xls')
while True:
    try:
        shutil.move('C:/Users/hs703/Downloads'+'/K-stat 총괄 .xls', 'C:/Users/hs703/Desktop/kjeon'+'/Kstat_FileDir') # path + '/K-stat 총괄 .xls' 이 경로의 파일을 path+'/fileDir' 이 경로의 해당 폴더 안으로 이동시켜주세요
        #shutil.move('C:/Users/kjeon0901/Downloads'+'/K-stat 총괄 .xls', 'C:/Users/kjeon0901/Desktop/21proj/study/python-WebScraping-WebCrawling'+'/Kstat_FileDir') # path + '/K-stat 총괄 .xls' 이 경로의 파일을 path+'/fileDir' 이 경로의 해당 폴더 안으로 이동시켜주세요
        break
    except:
        print('이동실패')
        time.sleep(1)
os.rename('C:/Users/hs703/Desktop/kjeon/Kstat_FileDir'+'/K-stat 총괄 .xls', 'C:/Users/hs703/Desktop/kjeon/Kstat_FileDir'+'/K-stat file_'+num+'.xls')
#os.rename('C:/Users/kjeon0901/Desktop/21proj/study/python-WebScraping-WebCrawling/Kstat_FileDir'+'/K-stat 총괄 .xls', 'C:/Users/kjeon0901/Desktop/21proj/study/python-WebScraping-WebCrawling/Kstat_FileDir'+'/K-stat file_'+num+'.xls')

temp = []
temp.append(data)

while True:
    try:
        driver.find_element_by_xpath("//strong[@class='selected']/following-sibling::a[1]").click()
    except:
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/a[2]").click()
        time.sleep(5)
        bs = BeautifulSoup(driver.page_source) 
        if bs.find('strong', {'class':'selected'}).get_text() == '53':
            # 여기서 프로그램 종료 안 되고 에러나면서 끝남. 해결 필요!
            break
        else:
            last_1stPage = bs.find('strong', {'class':'selected'}).get_text()
    time.sleep(5)
    
    # 파일다운 + 이동 + 이름변경해서 폴더 안에 저장
    bs = BeautifulSoup(driver.page_source) 
    num = bs.find('strong', {'class':'selected'}).get_text()
    while True:
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/form/div[1]/div/a[1]').click()
        time.sleep(3)
        data = pd.read_excel('C:/Users/hs703/Downloads/K-stat 총괄 .xls') #이 경로의 파일을 열고 불러와 객체로 f에 담기 (더블클릭 따닥-!)
        if data.shape[0] >= 103 and data.shape[1] >= 13:
            print('num', num, '성공')
            break
        elif bs.find('strong', {'class':'selected'}).get_text() == '53':
            print('num', num, '성공')
            break
            
        
        print('num', num, '실패')
        os.remove('C:/Users/hs703/Downloads/K-stat 총괄 .xls')
    temp.append(data)
    while True:
        try:
            shutil.move('C:/Users/hs703/Downloads'+'/K-stat 총괄 .xls', 'C:/Users/hs703/Desktop/kjeon'+'/Kstat_FileDir') # path + '/K-stat 총괄 .xls' 이 경로의 파일을 path+'/fileDir' 이 경로의 해당 폴더 안으로 이동시켜주세요
            #shutil.move('C:/Users/kjeon0901/Downloads'+'/K-stat 총괄 .xls', 'C:/Users/kjeon0901/Desktop/21proj/study/python-WebScraping-WebCrawling'+'/Kstat_FileDir') # path + '/K-stat 총괄 .xls' 이 경로의 파일을 path+'/fileDir' 이 경로의 해당 폴더 안으로 이동시켜주세요
            break
        except:
            print('이동실패')
            time.sleep(1)
    os.rename('C:/Users/hs703/Desktop/kjeon/Kstat_FileDir'+'/K-stat 총괄 .xls', 'C:/Users/hs703/Desktop/kjeon/Kstat_FileDir'+'/K-stat file_'+num+'.xls')
    #os.rename('C:/Users/kjeon0901/Desktop/21proj/study/python-WebScraping-WebCrawling/Kstat_FileDir'+'/K-stat 총괄 .xls', 'C:/Users/kjeon0901/Desktop/21proj/study/python-WebScraping-WebCrawling/Kstat_FileDir'+'/K-stat file_'+num+'.xls')

    

'''
os.walk(path) : 하위의 폴더들을 for문으로 탐색. 인자로 전달된 path에 대해서 (root, dirs, files)를 담은 tuple을 넘겨줌

root : dir과 files가 있는 path
dirs : root 아래에 있는 폴더들
files : root 아래에 있는 파일들
'''

temp = os.walk('C:/Users/hs703/Desktop/kjeon/Kstat_FileDir') # for문을 돌리는 용도로 사용된 객체
total = []
for idx, row in enumerate(temp):
    for row in row[2]: #모든 파일 각각
        total.append(pd.read_excel('C:/Users/hs703/Desktop/kjeon/Kstat_FileDir/' + row))
        # read_excel로 파일 불러올 때 header로 column name 정해줄 수 있음. 



# 컬럼 이름 중복되면 안 됨. 
df = pd.concat([each.iloc[:, 1:].drop(0) for each in total])
changeTo = df.iloc[[0, 1]].apply(lambda x : x.iloc[1] if x.iloc[0] == x.iloc[1] else str(x.iloc[0])+str(x.iloc[1]))
colname = dict(zip(list(df.columns), [each for each in changeTo]))
df_ = df.rename(columns = colname).drop([1, 2]).reset_index().drop('index', axis=1)












