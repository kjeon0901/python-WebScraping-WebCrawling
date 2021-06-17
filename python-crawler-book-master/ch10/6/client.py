import requests as rq
url = 'http://127.0.0.1:5000'
res1 = rq.get(url + '/test/data')
res2 = rq.get(url + '/api1', params={'data': 'get_data'})
res3 = rq.post(url + '/api2', data={'data': 'post_data'})
print(res1)
print(res2)
print(res3)
print(res1.url)
print(res2.url)
print(res3.url)
print(res1.content)
print(res2.content)
print(res3.content)