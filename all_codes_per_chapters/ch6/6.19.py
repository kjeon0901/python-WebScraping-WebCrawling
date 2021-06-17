import requests as rq

url = "https://pjt3591oo.github.io/"

res = rq.get(url, params={"key1": "value1", "key2": "value2"})

print(res.url)
