import requests as rq

url = "http://localhost:3000"

res = rq.get(url)

print(res)
print(res.text)
