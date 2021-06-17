import pandas as pd

df = pd.read_csv('test.csv')

print(df.ix[1:4, :2]) # .ix[로우 슬라이싱, 컬럼 슬라이싱]
