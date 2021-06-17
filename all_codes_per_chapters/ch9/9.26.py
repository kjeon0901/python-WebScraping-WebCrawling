import pandas as pd

df = pd.read_csv('test.csv')

print('상위 데이터만 출력')
print(df.head())

print('하위 데이터만 출력')
print(df.tail())
