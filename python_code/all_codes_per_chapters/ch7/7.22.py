from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p><span>test1</span><span>test2</span></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

tag_span = soup.span
tag_title = soup.title

span_parents = tag_span.parents
title_parents = tag_title.parents

print('태그')
print(tag_span)
print(tag_title)

print('부모태그')
print(span_parents)
print(title_parents)
