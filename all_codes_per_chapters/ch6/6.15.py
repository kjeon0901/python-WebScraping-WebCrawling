import requests as rq

url = "http://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)

cookies = list(res.cookies)
headers_cookies = res.headers['Set-Cookie']

print('cookies 속성')
print(cookies)
print('')
print('headers 속성')
print(headers_cookies)
