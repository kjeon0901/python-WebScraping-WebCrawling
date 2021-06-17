from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p>test1</p><p id="d">test2</p><p>test3</p></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all(id = True))
print(soup.body.find_all(id = False))
