from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p><a>test1</a><b>test2</b><c>test3</c></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

tag_a = soup.a
tag_a_nexts = tag_a.next_elements

for i in tag_a_nexts:
    print(i)
