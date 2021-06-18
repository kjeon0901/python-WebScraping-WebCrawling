import requests as rq

url = "https://github.com/kjeon0901/"

res = rq.get(url)

print(res.content)
