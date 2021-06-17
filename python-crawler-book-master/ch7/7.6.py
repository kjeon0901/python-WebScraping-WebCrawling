import time
from bs4 import BeautifulSoup

html = """<html><head></head><p>test</p></html>"""

start_time = time.time()
BeautifulSoup(html, 'lxml')
lxml_end_time = time.time() - start_time

start_time = time.time()
BeautifulSoup(html, 'html5lib')
html5lib_end_time = time.time() - start_time

print('lxml 시간측정 : %f'%(lxml_end_time))
print('html5lib 시간측정 : %f'%(html5lib_end_time))
print(html5lib_end_time / lxml_end_time)
