import requests as rq

url = "blog.naver.com/pjt3591oo"

try:
    res = rq.get(url)
except rq.exceptions.MissingSchema:
    print('MissingSchema 에러 발생')
