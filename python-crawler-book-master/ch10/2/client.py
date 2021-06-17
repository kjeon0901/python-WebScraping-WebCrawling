import requests as rq

url = 'http://127.0.0.1:5000'

res = rq.get(url)

print(res)
print(res.content)
