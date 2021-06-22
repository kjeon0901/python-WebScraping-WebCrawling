from selenium import webdriver

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('chromedriver') # 빈 브라우저 띄움
driver.get(url) # url 접속
