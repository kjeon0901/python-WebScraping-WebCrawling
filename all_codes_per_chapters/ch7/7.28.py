from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p><a>ttt<span>123</span><span>123</span></a><b>test2</b><c>test3</c></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

tag_p_nexts = soup.p.next_elements

print(soup.prettify())
print('**elements**')

for i in tag_p_nexts:
    print(i)
