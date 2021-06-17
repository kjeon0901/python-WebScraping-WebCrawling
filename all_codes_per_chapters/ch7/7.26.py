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

tag_a_nexts = tag_a.next_siblings
tag_a_prevs = tag_c.previous_siblings

print(tag_a_nexts)
print(tag_a_prevs)

print('next siblings')
for sibling in tag_a_nexts:
    print(sibling)

print('previous siblings')
for sibling in tag_a_prevs:
    print(sibling)
