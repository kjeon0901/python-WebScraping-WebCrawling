from bs4 import BeautifulSoup

html = """<html><p>test</p></html>"""
soup = BeautifulSoup(html, 'lxml')
print(soup)

html = """<body><p>test</p></body>"""
soup = BeautifulSoup(html, 'lxml')
print(soup)
