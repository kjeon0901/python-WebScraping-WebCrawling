import requests as rq

url = "https://blog.naver.com/kjeon0901"

res = rq.get(url)

print(res)

cookies = res.cookies
print(cookies)
'''
<RequestsCookieJar[<Cookie JSESSIONID=EB17C42065676C826ED5710E0E18AE21.jvm1 for blog.naver.com/>]>
내가 접속한 블로그에 대한 쿠키 파일이 남았다. 
'''