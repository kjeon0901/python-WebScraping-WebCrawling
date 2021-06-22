from selenium import webdriver

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

selected_selector = driver.find_element_by_css_selector('.a')
print(selected_selector)
print(selected_selector.tag_name)
print(selected_selector.text)
