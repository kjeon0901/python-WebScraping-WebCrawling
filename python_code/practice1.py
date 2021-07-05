import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 크롤링한 데이터를 csv 파일에 저장하는 코드

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')
# The main comparison table is currently the first table on the page
table = bs.findAll('table',{'class':'wikitable'})[0]
rows = table.findAll('tr')
'''
table은 사실상 csv로 저장하기 가장 좋은 형태. 
애초에 형태 자체가 똑같으므로 어떤 방식으로 저장할지에 대한 고민 없이 그대로 긁어서 저장하면 됨.
'''

csvFile = open('editors.csv', 'wt+', encoding='UTF-8') # 인코딩 방식 때문에 에러나는 것 해결 위해 encoding='UTF-8' 추가
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']): # th : tr의 인덱스같은 존재, td : tr 안의 데이터
            csvRow.append(cell.get_text())
        writer.writerow(csvRow) # editors.csv에서 하나의 row에 csvRow 써줌
finally: # 예외처리 try-except-finally : try문 수행 도중 예외가 발생했든 아니든(try문 수행하든 except문 수행하든) finally문 항상 수행
    csvFile.close()