import requests as rq

url = 'https://avatars2.githubusercontent.com/u/12229295?v=4&s=60'

res = rq.get(url)

with open('t.png', 'wb') as f:
    f.write(res.content)
