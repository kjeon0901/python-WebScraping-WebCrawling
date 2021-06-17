from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p id="i" class="a">test1</p><p class="d">test2</p><p class="d">test3</p></p> <a>a tag</a> <b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.select('p'))
print(soup.select('.d'))
print(soup.select('p.d'))
print(soup.select('#i'))
print(soup.select('p#i'))
