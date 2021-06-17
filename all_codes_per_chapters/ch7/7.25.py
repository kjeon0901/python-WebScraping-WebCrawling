from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p><a>test1</a><b>test2</b><c>test3</c></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

tag_a = soup.a
tag_b = soup.b
tag_c = soup.c

print('tags')
print(tag_a)
print(tag_b)
print(tag_c)

tag_a_next = tag_a.next_sibling
tag_a_prev = tag_a.previous_sibling

tag_b_next = tag_b.next_sibling
tag_b_prev = tag_b.previous_sibling

tag_c_next = tag_c.next_sibling
tag_c_prev = tag_c.previous_sibling

print('siblings')
print(tag_a_next)
print(tag_a_prev)

print(tag_b_next)
print(tag_b_prev)

print(tag_c_next)
print(tag_c_prev)
