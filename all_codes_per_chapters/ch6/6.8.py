import requests as rq

url = "https://blog.naver.com/kjeon0901"

res = rq.get(url)

print(res)
print(res.headers) # 딕셔너리 타입 
print(len(res.headers))
'''
<Response [200]>
{'Date': 'Fri, 18 Jun 2021 01:06:04 GMT', 'Content-Type': 'text/html;charset=UTF-8', 'Transfer-Encoding': 'chunked', 
 'Connection': 'close', 'Vary': 'Accept-Encoding', 'Cache-Control': 'no-cache', 'Expires': 'Thu, 01 Jan 1970 00:00:00 GMT', 
 'Set-Cookie': 'JSESSIONID=7A8C9A4666E68B5D11A123D946BF986B.jvm1; Path=/; Secure; HttpOnly', 'Content-Encoding': 'gzip', 
 'Server': 'nxfps', 'Referrer-policy': 'unsafe-url'}
11
'''