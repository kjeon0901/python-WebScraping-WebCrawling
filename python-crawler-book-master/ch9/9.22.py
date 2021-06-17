columns = ["이름", "나이", "주소"]

names = ["철구", "맹구", "짱구", "유리"]
ages = ["20", "21", "20", "22"]
address = ["경기도", "강원도", "경상도", "전라도"]

with open("ch.9.22.csv", "a") as f:
    column = ','.join(columns) + '\n'
    f.write(column)

    for i in range(0, len(names)):
        row = ('%s, %s, %s\n')%(names[i], ages[i], address[i])
        f.write(row)
