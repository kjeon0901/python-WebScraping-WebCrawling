from selenium import webdriver

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

driver.execute_script('alert("test")')

for i in range(0, 100):
    print(i)
