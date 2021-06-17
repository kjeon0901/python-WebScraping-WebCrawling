from slackclient import SlackClient
import time

slack_token = '발급받은 토큰'
sc = SlackClient(slack_token)

# 메시지 전달
def notification(message, sc):
    sc.api_call(
        "chat.postMessage",
        channel="#general",
        text=message
    )

# 유저가 보낸 메시지 인지 파이썬이 응답한 메시지인지 검사
def is_user(k):
    return 'type' in k and 'text' in k and 'user' in k

def is_receive(data):
    return len(data)

# RTM
if sc.rtm_connect():
    while True:
        receive_data = sc.rtm_read()
        if is_receive(receive_data):
            keys = list(receive_data[0].keys())
            if is_user(keys):
                message = receive_data[0]['text']
                print(receive_data)
                notification(message + ' response', sc)

        time.sleep(1)
else:
    print("Connection Failed")
