import pandas as pd

dict_data = {'c0':[1, 2, 3], 'c1':[4, 5, 6]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df, "\n")

col0 = df['c0']
col1 = df.c1

print(col0, "\n")
print(col1, "\n")

df['c2'] = 7, 8, 9
print(df, "\n")

df['c3'] = 0
print(df, "\n")

df['c4'] = df['c3']
print(df, "\n")

df['c3'] = 10, 11, 12
print(df, "\n")

df['c3'] = 0
print(df, "\n")

df.drop('c4', axis=1, inplace=True)
print(df, "\n")

df.drop(['c1', 'c3'], axis=1, inplace=True)
print(df, "\n")
