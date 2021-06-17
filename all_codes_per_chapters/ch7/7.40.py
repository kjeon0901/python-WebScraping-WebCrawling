from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p>test1</p><p class="d">test2</p><p class="c">test3</p></p> <a>a tag</a> <b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

tag_body = soup.find_all('body')
tag_p = tag_body[0].find_all('p')

print(type(tag_body), tag_body)
print(type(tag_p), tag_p)
