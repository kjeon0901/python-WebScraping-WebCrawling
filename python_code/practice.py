import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import time

# url = 'https://www.naver.com'
url = 'https://news.naver.com'

var = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
# 네이버에서 F12 - Network - 새로고침 - Headers - Request Headers - user-agent 가져와서 이렇게 key, value값으로 넣어줌
html3 = requests.get(url, headers = var) # 그 정보를 headers로 넣어줌. 
bs = BeautifulSoup(html3.text)
print(html3.request.headers)
'''
{'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
--------------------------------------------------------------------------------------
User-Agent
    - 아까와 다르게 'python-requests/2.24.0'이 아니라 '~~~ Chrome/91.0.4472.114 Safari/537.36'이 들어 있으므로
      "내가 크롬이다!"라는 걸 알려주면서 네이버에 접근하게 되는 것!

=> 우회 잘 되었군!
url = 'https://www.naver.com'
url = 'https://news.naver.com'
둘 다 잘 접근 잘 된다. 
'''