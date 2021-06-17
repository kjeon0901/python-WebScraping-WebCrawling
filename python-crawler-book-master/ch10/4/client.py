import requests as rq

url = 'http://127.0.0.1:5000'

get_res1 = rq.get(url)
get_res2 = rq.get(url + '/api1')
get_res3 = rq.get(url + '/api2')

post_res1 = rq.post(url)
post_res2 = rq.post(url + '/api1')
post_res3 = rq.post(url + '/api2')

print(get_res1)
print(get_res2)
print(get_res3)

print(get_res1.content)
print(get_res2.content)
print(get_res3.content)

print(post_res1)
print(post_res2)
print(post_res3)

print(post_res1.content)
print(post_res2.content)
print(post_res3.content)
