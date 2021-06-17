import pandas as pd

df = pd.read_csv('test.csv')

name = df['나이']
age = df['이름']

print('axis가 1일 때')
p1 = pd.concat([name, age], axis=1)
print(p1)

print('\naxis가 0일 때')
p2 = pd.concat([name, age], axis=0)
print(p2)
