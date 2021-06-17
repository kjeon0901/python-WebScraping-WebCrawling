from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p><span>test1</span><span>test2</span></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

tag_p_child = soup.p.children

for child in tag_p_child:
    print(child)
