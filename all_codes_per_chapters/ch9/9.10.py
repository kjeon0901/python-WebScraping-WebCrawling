# 메시지 전달
from slackclient import SlackClient

def notification(message):
    slack_token = '발급받은 토큰'
    sc = SlackClient(slack_token)
    sc.api_call(
        "chat.postMessage",
        channel="#general",  # {#채널}의 형태로 채널 지정
        text=message
    )

notification('test')
