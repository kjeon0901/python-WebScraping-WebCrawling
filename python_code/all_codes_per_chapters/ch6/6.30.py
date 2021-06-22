from urllib.request import urlopen, Request

url = "https://pjt3591oo.github.io/"

req = Request(url)
page = urlopen(req)

print(page)
print(page.read())
