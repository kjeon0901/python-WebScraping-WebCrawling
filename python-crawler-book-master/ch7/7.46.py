from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <div><p id="i" class="a">test1</p><p class="d">test2</p></div><p class="d">test3</p></p> <a>a tag</a> <b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.select('body p'))
print(soup.select('body .d'))
print(soup.select('body p.d'))
print(soup.select('body #i'))
print(soup.select('body p#i'))

print(soup.select('div p'))
