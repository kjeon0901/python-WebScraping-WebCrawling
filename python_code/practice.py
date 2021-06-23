from selenium import webdriver
import time

#### Selenium으로 url 자동으로 열어 검색창에 검색해보기


driver = webdriver.Chrome('C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe')
url1 = 'https://www.naver.com'
url2 = 'https://www.google.com'
url3 = 'https://github.com/kjeon0901'

driver.get(url1)
# 네이버 검색창 input id : query
n_search_box = driver.find_element_by_id("query")
n_search_box.send_keys("크루엘라 평점") # 검색할 문자열을 키로 보낸 후
n_search_box.submit() # 검색버튼 눌러줌
time.sleep(1)

driver.get(url2)
# 구글 검색창 input name : q
g_search_box = driver.find_element_by_name("q")
g_search_box.send_keys("빌보드 차트 순위")
g_search_box.submit()
time.sleep(1)

driver.get(url3)
time.sleep(1)
driver.quit()
