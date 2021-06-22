import requests as rq

url = "https://blog.naver.com/kjeon0901"

res = rq.get(url)

print(res)

headers = res.headers

for header in headers:
    print(headers[header])
'''
<Response [200]>
Fri, 18 Jun 2021 01:16:38 GMT
text/html;charset=UTF-8
chunked
close
Accept-Encoding
no-cache
Thu, 01 Jan 1970 00:00:00 GMT
JSESSIONID=C62E32687DD25DC10E313A7B5DD396E0.jvm1; Path=/; Secure; HttpOnly
gzip
nxfps
unsafe-url
'''