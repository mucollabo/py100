import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/bok_statistics_CD_2.csv', header=0, index_col=0)
print(df.head())
print('\n')

boxplot = df.plot(kind='box')
plt.savefig('./output/boxplot.png')