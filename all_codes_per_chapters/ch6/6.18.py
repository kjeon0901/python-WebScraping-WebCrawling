import requests as rq

url = "https://github.com/kjeon0901/"

res = rq.get(url)

print(res.encoding) # utf-8형식으로 인코딩돼있구나~ 그럼 똑같이 utf-8로 디코딩해야겠구나~
'''utf-8'''