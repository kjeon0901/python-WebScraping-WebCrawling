from selenium import webdriver

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

selected_selector = driver.find_element_by_css_selector('div.home div.p a')
print(selected_selector.tag_name)
print(selected_selector.text)
selected_selector.click()
