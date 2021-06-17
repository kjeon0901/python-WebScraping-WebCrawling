import pandas as pd

df = pd.read_csv('test.csv')

print(df.ix[:, 1])
print(df.ix[1, 1])
print(df.ix[1, 2])
