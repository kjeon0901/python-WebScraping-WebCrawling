import requests as rq

url1 = "https://aldkfja.com/kjeon0901/a" # https://aldkfja.com/kjeon0901 라는 서버에서 a라는 웹페이지
res1 = rq.get(url1)
print(res1)
print(res1.status_code)
'''error'''

url2 = "https://github.com/kjeon0901/a" # https://github.com/kjeon0901 라는 서버에서 a라는 웹페이지
res2 = rq.get(url2)
print(res2)
print(res2.status_code)
'''
<Response [404]>
404

서버 : https://github.com/kjeon0901
페이지 : https://github.com/kjeon0901/python-spider-machinelearning

url1. 서버 주소 자체를 잘못 입력한 경우 => '사이트에 연결할 수 없음', 코드 상으로는 아예 에러 남. 
url2. 서버에 들어갔는데 페이지가 없는 경우 => 404 뜸. 

프로그램이 돌다가 찾는 페이지 없어서 넘어가면 괜찮지만, 아예 에러가 나서 멈춰 있으면 안되니까 try-catch문 多 써줌! 
'''

