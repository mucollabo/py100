import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/bok_statistics_CD_2.csv', header=0, index_col=0)
print(df.head())
print('\n')

df.plot(x='CD_rate', y='change', kind='scatter')
plt.show()