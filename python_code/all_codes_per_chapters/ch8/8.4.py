from selenium import webdriver

url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('C:/Users/hs-702/Desktop/kjeon/chromedriver_win32/chromedriver.exe')
driver.get(url) # url 열어줌

selected_tag_p = driver.find_element_by_tag_name('p') # find()
print(selected_tag_p) # 태그 자체 출력
print(selected_tag_p.tag_name) # 해당 태그의 이름
print(selected_tag_p.text) # 해당 태그 안에 들어 있는 text

selected_tags_p = driver.find_elements_by_tag_name('p') # find_all()
print(selected_tags_p)
