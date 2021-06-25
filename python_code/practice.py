import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import time

url = 'https://www.naver.com'
'''
url = 'https://news.naver.com' 로 바꾸면 => Remote end closed connection without response 에러 뜸. 
url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=448&aid=0000332119' 이렇게 기사 하나 접근해도 에러 뜸. 
★★★ 우회가 필요하다!! ★★★

'''
html = urlopen(url)
print(html.headers)
'''
Server: NWS
Date: Fri, 25 Jun 2021 01:44:33 GMT
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: close
Set-Cookie: PM_CK_loc=3232355beb513edf3f28c441f6ad912584637d53608e6f52db25aa25b48df3fb; Expires=Sat, 26 Jun 2021 01:44:33 GMT; Path=/; HttpOnly
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
P3P: CP="CAO DSP CURa ADMa TAIa PSAa OUR LAW STP PHY ONL UNI PUR FIN COM NAV INT DEM STA PRE"
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=63072000; includeSubdomains
Referrer-Policy: unsafe-url
'''