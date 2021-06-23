from selenium import webdriver

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe') # 빈 브라우저 띄움
driver.get(url) # url 접속
