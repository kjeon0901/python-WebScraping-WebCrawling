import requests as rq

url = "http://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)

headers = res.headers

for header in headers:
    print(headers[header])
