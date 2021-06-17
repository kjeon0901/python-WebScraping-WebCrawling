from bs4 import BeautifulSoup

html = """<p>test</p>"""

soup = BeautifulSoup(html, 'lxml')
print(soup)
