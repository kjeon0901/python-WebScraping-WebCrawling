from urllib.request import urlopen, Request
import urllib

url = "http://blog.naver.com/pjt3591oo"

# post 요청 시 보낼 데이터 만들기
data = {'key1': 'value1', 'key2': 'value2'}
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')

print(data)

# post 요청
req_post = Request(url, data=data, headers={})  # 2번쨰 인자 데이터, 세 번째 인자 헤더
page = urlopen(req_post)

print(page)
print(page.url)

# get 요청
req_get = Request(url+"?key1=value1&key2&value2", None, headers={})  # 2번쨰 인자 데이터, 세 번째 인자 헤더
page = urlopen(req_get)

print(page)
print(page.url)
