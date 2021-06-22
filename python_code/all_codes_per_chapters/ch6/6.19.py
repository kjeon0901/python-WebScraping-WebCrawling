import requests as rq

url = "https://github.com/kjeon0901/"

res1 = rq.get(url, params={"key1": "value1", "key2": "value2"}) # query string 

print(res1.url)
'''
https://github.com/kjeon0901/?key1=value1&key2=value2

일반적으로 get 명령어에서는 파라미터 설정값을 url주소에다가 한꺼번에 붙여서 넘겨주는 방식 多 사용. 
- 딕셔너리 형태. 

어떤 설정값을 주느냐에 따라 웹페이지 정보가 바뀜. 

네이버 로그인
https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com
mode    form
url     https%3A%2F%2Fwww.naver.com

네이버 일회용 번호 로그인
https://nid.naver.com/nidlogin.login?mode=number&url=https%3A%2F%2Fwww.naver.com&locale=ko_KR&svctype=1
mode    number
url     https%3A%2F%2Fwww.naver.com
locale  ko_KR
svctype 1

'''