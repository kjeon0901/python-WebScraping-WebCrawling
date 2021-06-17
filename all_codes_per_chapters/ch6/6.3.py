import requests as rq

url = "https://github.com/kjeon0901"

test = rq.get(url) # rq가 url에 get메시지를 보냄. 
                   # chrome, explorer 등 웹 브라우저를 거치지 않고 url이라는 서버에 접근해서 url웹페이지에 대한 코드를 가져옴. 
'''
파이썬에서는 그냥 rq가 url에 get메시지를 보낸 것 하나지만, 
서버에서는 해당 url에 대한 코드 html, css, javascript 등등을 보내주고, 그걸 실행함으로써 알아서 웹페이지가 열렸다. 

이제는 받아온 데이터 test에서 원하는 정보를 추출할 것임 !!
'''
