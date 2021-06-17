from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p>test</p> <p>test1</p> <p>test2</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
