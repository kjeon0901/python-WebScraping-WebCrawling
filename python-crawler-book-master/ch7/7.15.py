from bs4 import BeautifulSoup

html = """<html> <head><title class="t" id="ti">test site</title></head> <body> <p>test</p> <p>test1</p> <p>test2</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_title = soup.title

print(tag_title.attrs)
print(tag_title.get('class'))
print(tag_title.get('id'))
print(tag_title.get('class1'))
print(tag_title.get('class1', 'default_value'))
