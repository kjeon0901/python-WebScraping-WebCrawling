from selenium import webdriver

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe')
driver.get(url)

selected_id = driver.find_element_by_id('nav-trigger')
print(selected_id)
print(selected_id.tag_name)
print(selected_id.text)

driver.find_element_by_xpath('/html/body/header/div/nav/div/a[1]').click() # about 페이지 클릭해서 넘어감
