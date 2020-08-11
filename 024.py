import pandas as pd

dict_data = {'c0':[1, 2, 3], 'c1':[4, 5, 6]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df, "\n")

df.to_csv("./output/df.csv")

df.to_excel("./output/df.xlsx")