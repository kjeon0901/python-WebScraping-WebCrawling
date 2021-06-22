from selenium import webdriver

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

selected_tags_a = driver.find_elements_by_css_selector('a')

for i in selected_tags_a:
    print(i.text, i.tag_name)
    i.click()
