import requests as rq

url = "https://pjt3591oo.github.io//?key2=value2&key1=value1"

res = rq.get(url)

print(res.url)
