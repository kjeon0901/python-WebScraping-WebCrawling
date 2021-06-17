import requests as rq

url = 'http://127.0.0.1:5000'

res1 = rq.get(url + '/123')
print(res1)
print(res1.text)
