from bs4 import BeautifulSoup

def remove_tag(soup, tags):
    if tags == []:
        return False

    removes = []

    for tag in soup.find_all(tags):
        removes.append(tag.extract())

    return removes

html = """<html> <head><title>test site</title></head> <body> <div><p id="i" class="a">test1</p><p class="d">test2</p></div><p class="d">test3</p></p> <a>a tag</a> <b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

removed_tag = remove_tag(soup, [])
print(removed_tag)
print(soup)
