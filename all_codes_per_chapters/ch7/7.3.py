from bs4 import BeautifulSoup

html = """<p>test</p>"""

soup = BeautifulSoup(html, 'html5lib')
print(soup)
