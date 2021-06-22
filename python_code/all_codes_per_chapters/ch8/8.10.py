from selenium import webdriver

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

selected_selector = driver.find_element_by_css_selector('div.home div.p')
print(selected_selector)
print(selected_selector.tag_name)
print(selected_selector.text)

selected_selectors = driver.find_element_by_css_selector('div.home div.p')
print(selected_selectors)
