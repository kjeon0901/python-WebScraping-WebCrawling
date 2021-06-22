import requests as rq
import time

url = "http://blog.naver.com/pjt3591oo"
delay_time = 1

def connection(u):
    return rq.get(u)

try:
    connection(url)

except rq.exceptions.Timeout:
    time.sleep(delay_time)
    connection(url)
