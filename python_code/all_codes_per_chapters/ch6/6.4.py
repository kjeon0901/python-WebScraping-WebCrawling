import requests as rq

url = "https://github.com/kjeon0901"

res = rq.get(url)
print(res)
print(res.status_code)
'''
<Response [200]>
200


내가 어떤 요청을 하고 그게 수행되면 연산 결과 or 상태메시지에 대한 '응답 코드'가 온다. 
<Response [200]>    - 정상적으로 작동했다. 
                    - ex_ 로그인할 때 id, password를 입력하고 로그인 버튼 누르면, id, password를 담은 메시지가 request로 가고, 회원정보에 해당되면 200 반환
<Response [201]>    - 정상적으로 저장되었다. 
<Response [401]>    - 권한이 없다. 
... 수많은 응답 코드가 있으므로 외우지 말고 그때그때 찾아보자!

=> 웹크롤링 하는 도중 문제 해결이 필요하다면 웹에 대한 이런 기본 지식이 필요하다. 
'''