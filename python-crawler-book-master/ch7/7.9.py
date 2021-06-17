from bs4 import BeautifulSoup

html = """<html> <head> </head> <body> <p>test</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
print(soup)
print(type(soup))
