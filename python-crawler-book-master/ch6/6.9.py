import requests as rq

url = "http://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)

headers = res.headers
print(headers['Set-Cookie'])
