import time
from bs4 import BeautifulSoup

html = """<html><head></head><p>test</p></html>"""

time_sum = 0
loop_count = 5

for i in range(0, loop_count):

    start_time = time.time()
    BeautifulSoup(html, 'lxml')
    lxml_end_time = time.time() - start_time

    start_time = time.time()
    BeautifulSoup(html, 'html5lib')
    html5lib_end_time = time.time() - start_time

    rate = html5lib_end_time / lxml_end_time

    print("%d 번째 시도" %(i))
    print('lxml 시간측정 : %f' %(lxml_end_time))
    print('html5lib 시간측정 : %f' %(html5lib_end_time))
    print('**', rate, '**\n')
    time_sum += rate

average = time_sum / loop_count
print('평균속도 : %f' %(average))
