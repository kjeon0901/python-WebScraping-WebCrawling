import requests as rq

url = "https://pjt3591oo.github.io/a"

res = rq.get(url)

print(res)
print(res.status_code)
