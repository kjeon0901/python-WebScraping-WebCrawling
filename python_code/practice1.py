from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
import time

#### Selenium으로 네이버 자동 로그인해보기


path = 'C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe'
url = 'https://naver.com'

id_ = ""
pw_ = ""

# 크롬 옵션 정의 (1이 허용, 2가 차단)
chrome_options = Options() 
prefs = {"profile.default_content_setting_values.notifications": 2} 
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(path, options=chrome_options)
driver.get(url)

click = driver.find_element_by_class_name("link_login")
click.click()
login_box = driver.find_element_by_id("id")
login_box.send_keys(id_)
time.sleep(1)
login_box = driver.find_element_by_id("pw")
login_box.send_keys(pw_)
time.sleep(1)
login_box.send_keys(Keys.RETURN) # Keys.ENTER도 가능
time.sleep(1) 

driver.quit()







