from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p><span>test1</span><span>test2</span></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_p = soup.p

data_text = tag_p.text
data_string = tag_p.string

print('text : ', data_text, type(data_text))
print('string : ', data_string, type(data_string))
