import requests as rq
from bs4 import BeautifulSoup

def get_posts(soup):
    return soup.select('body main.page-content div.wrapper div.home div.p')

def data_parse(posts):
    for post in posts:
        title = post.find('h3').text.strip()
        descript = post.find('h4').text.strip()
        author = post.find('span').text.strip()
        print(title, descript, author)

base_url = 'https://pjt3591oo.github.io'
page_path = '/page%d'
page = 2

res = rq.get(base_url)
soup = BeautifulSoup(res.content, 'lxml')

posts = get_posts(soup)
data_parse(posts)

while True:
    sub_path = page_path%(page)
    page += 1
    res = rq.get(base_url + sub_path)

    if (res.status_code != 200):
        break

    soup = BeautifulSoup(res.content, 'lxml')
    posts = get_posts(soup)

    data_parse(posts)
