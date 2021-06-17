from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p><span>test1</span><span>test2</span></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

tag_span = soup.span
tag_title = soup.title

span_parent = tag_span.parent
title_parent = tag_title.parent

print('태그')
print(tag_span)
print(tag_title)

print('부모태그')
print(span_parent)
print(title_parent)
