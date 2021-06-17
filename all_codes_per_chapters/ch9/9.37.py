import pandas as pd

df = pd.read_csv('test.csv')

print(df['나이']==1)   # 나이는 숫자가 들어있기 때문 에 '1'로 하면 에러 발생
print(df['이름']==1)   # 문자형으로 저장 된 컬럼은 숫자, 문자로 필터해도 에러 없음
