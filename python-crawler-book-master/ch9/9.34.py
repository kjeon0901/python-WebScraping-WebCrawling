import pandas as pd

df = pd.read_csv('test.csv')

print(df[df['나이']> 30])
