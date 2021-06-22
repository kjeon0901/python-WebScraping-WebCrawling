import requests as rq

url = "https://blog.naver.com/kjeon0901"

res = rq.get(url)

print(res)

headers = res.headers
print(headers['Set-Cookie']) # 딕셔너리 타입에 접근할 때에는 key값 이용 !
'''
Cookie
- ex) 내가 어떤 브라우저에서 로그인 한 뒤, 브라우저 껐다가 다시 켰는데 그대로 로그인 되어 있는 경우 '쿠키' 때문!
- '내가 이 브라우저에 접속했다' 는 게 작은 txt파일로 서버가 아니라 내 컴퓨터의 브라우저에 저장되는 것. 
  그러면 내가 브라우저에 다시 접속하면, 브라우저가 그 txt파일을 서버에 보내줘서 로그인 바로바로 되게 해줌. 
- 그런데 보안이 문제! 내 브라우저를 해킹하면 문제! => 조심스럽다. 
'''