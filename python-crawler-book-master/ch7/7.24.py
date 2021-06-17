from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p><span>test1</span><span>test2</span></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

tag_span = soup.span

a = tag_span.next_sibling
b = a.previous_sibling

print(a)
print(b)
