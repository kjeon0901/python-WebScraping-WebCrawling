import requests as rq
from bs4 import BeautifulSoup
from slackclient import SlackClient

# 메시지 전달
def notification(message):
    slack_token = '발급받은 토큰'
    sc = SlackClient(slack_token)
    sc.api_call(
        "chat.postMessage",
        channel="#general",
        text=message
    )

base_url = 'https://pjt3591oo.github.io/'

res = rq.get(base_url)
soup = BeautifulSoup(res.content, 'lxml')

posts = soup.select('body main.page-content div.wrapper div.home div.p')

result = []

for post in posts:
    title = post.find('h3').text.strip()
    descript = post.find('h4').text.strip()
    author = post.find('span').text.strip()
    result.append(title)
    print(title, descript, author)

notification('%d개 데이터 수집완료'%len(result))
