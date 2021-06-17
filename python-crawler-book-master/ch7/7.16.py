from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p>test</p> <p>test1</p> <p>test2</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_title = soup.title

data_text = tag_title.text
data_string = tag_title.string

print('text : ', data_text, type(data_text))
print('string : ', data_string, type(data_string))
