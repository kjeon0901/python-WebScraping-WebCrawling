from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <div><p id="i" class="a">test1</p><p class="d">test2</p></div><p class="d">test3</p></p> <a>a tag</a> <b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

for tag in soup.select('p'):
    print(tag.extract())

print('제거완료')
print(soup)
