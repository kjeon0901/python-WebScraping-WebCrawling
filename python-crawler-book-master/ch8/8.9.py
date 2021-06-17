from selenium import webdriver

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

selected_class = driver.find_element_by_class_name('p')
print(selected_class)
print(selected_class.tag_name)
print(selected_class.text)

selected_classes = driver.find_elements_by_class_name('p')
print(selected_classes)
