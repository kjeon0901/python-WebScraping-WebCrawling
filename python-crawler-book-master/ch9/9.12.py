# RTM
from slackclient import SlackClient
import time

slack_token = ''
sc = SlackClient(slack_token)

if sc.rtm_connect():
    while True:
        receive_data = sc.rtm_read()
        print(receive_data)
        time.sleep(1)
else:
    print("Connection Failed")
