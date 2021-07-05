import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 크롤링한 데이터를 csv 파일에 저장하는 코드

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')
# The main comparison table is currently the first table on the page
table = bs.findAll('table',{'class':'wikitable'})[0]
rows = table.findAll('tr')

csvFile = open('editors.csv', 'wt+', encoding='UTF-8') # 인코딩 방식 때문에 에러나는 것 해결 위해 encoding='UTF-8' 추가
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()