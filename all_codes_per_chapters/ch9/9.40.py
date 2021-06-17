from pandas import DataFrame
import time

def test(i):
    print(("%d 번쨰 테스트")%(i))

    names = ['철구1', '맹구2', '짱구3', '유리4', '철구5', '맹구6', '짱구7', '유리8',]
    ages = [20, 21, 20, 12, 30, 31, 40, 30,]
    addresses = ['경기도', '강원도', '경상도', '전라도', '경기도', '강원도', '경상도', '전라도', ]

    data = {
        '이름': [],
        '나이': [],
        '주소': [],
    }

    data_length = 1000

    for i in range(0, data_length):
        data['이름'].extend(names)
        data['나이'].extend(ages)
        data['주소'].extend(addresses)

    data = DataFrame(data, columns=['나이', '주소', '이름'], index=data['주소'])

    print(data.head(3))

    start1 = time.time()
    new_add1 = data.ix['경기도']
    end1 = time.time() - start1

    start2 = time.time()
    new_add2 = data[data['주소'] == '경기도']
    end2 = time.time() - start2

    print('인덱스 검사 : %f'%(end1))
    print('컬럼 검사 : %f'%(end2))

    return {
        'index': end1,
        'column': end2
    }

index_sum = 0
column_sum = 0
count = 3

for i in range(count):
    d = test(i)
    column_sum += d['column']
    index_sum += d['index']


print('\n----- 검사결과 -----')
print('인덱스 검사 평균 : %s'%(index_sum/count))
print('컬럼 검사 평균 : %s'%(column_sum/count))
