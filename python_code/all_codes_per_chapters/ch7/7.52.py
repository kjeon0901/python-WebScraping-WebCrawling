from bs4 import BeautifulSoup
import re

html = """<html> <head><title>test site</title></head> <body> <div><p id="i" class="a">test1</p><p class="d">test2</p></div><p class="d">test3</p></p> <a href="/example/test1">a tag</a> <b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all(class_=re.compile('d')))
print(soup.find_all(id=re.compile('i')))
print(soup.find_all(re.compile('t')))
print(soup.find_all(re.compile('^t')))
print(soup.find_all(href=re.compile('/')))
