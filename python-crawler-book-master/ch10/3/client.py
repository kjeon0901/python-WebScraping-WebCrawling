import requests as rq

url = 'http://127.0.0.1:5000'

res1 = rq.get(url)
res2 = rq.get(url + '/api1')
res3 = rq.get(url + '/api2')

print(res1)
print(res2)
print(res3)

print(res1.content)
print(res2.content)
print(res3.content)
