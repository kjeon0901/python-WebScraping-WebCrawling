from urllib.request import urlopen, Request

url = "https://pjt3591oo.github.io/"

req = Request(url)
page = urlopen(req)

print(page)
print(page.code)
print(page.headers)
print(page.url)
print(page.info().get_content_charset())
