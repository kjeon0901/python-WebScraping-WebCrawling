from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p>test1</p><p>test2</p><p>test3</p></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all('title'))
print(soup.find_all('p'))
