from selenium import webdriver

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

selected_link = driver.find_element_by_partial_link_text('react')
print(selected_link)
print(selected_link.tag_name)
print(selected_link.text)

selected_links = driver.find_element_by_partial_link_text('react')
print(selected_links)
