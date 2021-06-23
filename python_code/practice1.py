from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
import time
import pyperclip 
# 네이버 캡차(로그인 자동 입력 방지) 우회하기 위한 라이브러리

#### Selenium으로 네이버 자동 로그인해보기


path = 'C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe'
url = 'https://naver.com'

id_ = ""
pw_ = ""

driver = webdriver.Chrome(path)
driver.get(url)

# 로그인 버튼 클릭
login_btn = driver.find_element_by_class_name("link_login")
login_btn.click()
time.sleep(1)

# id 입력
id_box = driver.find_element_by_id("id")
id_box.click()
time.sleep(1)
pyperclip.copy(id_)
id_box.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 입력
pw_box = driver.find_element_by_id("pw")
pw_box.click()
time.sleep(1)
pyperclip.copy(pw_)
pw_box.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
'''
cf. 
id, pw 입력할 때 아래처럼 send_keys( ) 사용하면 네이버 캡차(로그인 자동 입력 방지)에 걸림

login_box = driver.find_element_by_id("id")
login_box.send_keys(id_) 
time.sleep(1)
login_box = driver.find_element_by_id("pw")
login_box.send_keys(pw_)
time.sleep(1) # 시간이 너무 빠르면 자동툴로 인식하는 경우가 있어 계속 sleep 걸어줌
login_box.send_keys(Keys.RETURN) # Keys.ENTER도 가능
time.sleep(1) 
'''

# 로그인 버튼 클릭
login_btn = driver.find_element_by_id('log.login')
login_btn.click()

driver.quit()







