from selenium import webdriver

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

print(driver.page_source)
