import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn 제공 데이터셋 가져오기
df = sns.load_dataset('iris')
print(df.head())
print('\n')
print(df.columns.values)

