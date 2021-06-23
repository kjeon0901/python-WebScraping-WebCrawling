from selenium import webdriver

url = 'https://pjt3591oo.github.io/search'

driver = webdriver.Chrome('C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe')
driver.get(url)

selected_name = driver.find_element_by_name('query')
print(selected_name)
print(selected_name.tag_name)
print(selected_name.text)

selected_names = driver.find_elements_by_name('query')
print(selected_names)
