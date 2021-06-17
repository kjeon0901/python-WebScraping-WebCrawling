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

# RTM
if sc.rtm_connect():
    while True:
        receive_data = sc.rtm_read()
        if len(receive_data):
            keys = list(receive_data[0].keys())
            if 'type' in keys and 'text' in keys and 'user' in keys:
                message = receive_data[0]['text']
                print(receive_data)
                notification(message + ' response', sc)

        time.sleep(1)
else:
    print("Connection Failed")
