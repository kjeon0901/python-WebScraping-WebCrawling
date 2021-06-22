from urllib.request import urlopen, Request

url = "https://pjt3591oo.github.io/1"

req_post = Request(url)
page = urlopen(req_post)

print(page)
print(page.url)
