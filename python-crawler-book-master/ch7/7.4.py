from bs4 import BeautifulSoup

html = """<html><body><p>test</p></body></html>"""
soup = BeautifulSoup(html, 'html5lib')
print(soup)

html = """<html><head></head><p>test</p></html>"""
soup = BeautifulSoup(html, 'html5lib')
print(soup)

html = """<head></head><p>test</p>"""
soup = BeautifulSoup(html, 'html5lib')
print(soup)
