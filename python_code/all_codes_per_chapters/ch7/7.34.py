from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p>test1</p><p class="d">test2</p><p class="c">test3</p></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all('p', class_='d'))
print(soup.find_all('p', class_='c'))
