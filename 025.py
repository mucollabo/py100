import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/bok_statistics_CD.csv', header=None)
print(df.head())
print('\n')

df.columns = ['year', 'CD_rate', 'change']
df.set_index('year', inplace=True)
print(df.head())
df.to_csv('./data/bok_statistics_CD_2.csv')
print('\n')

df.plot()

df['CD_rate'].plot()
df['change'].plot()

plt.show()
