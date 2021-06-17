import requests as rq


def url_check(url):
    res = rq.get(url)

    print(res)

    sc = res.status_code

    if sc == 200:
        print("%s 요청성공"%(url))
    elif sc == 404:
        print("%s 찾을 수 없음" %(url))
    else:
        print("%s 알수 없는 에러 : %s"%(url, sc))


url_check("https://pjt3591oo.github.io/")
url_check("https://pjt3591oo.github.io//a")
