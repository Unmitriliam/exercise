import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# slupkowy z jednego roku, padding na dole

df = pd.read_excel('turystyka2.xlsx', header=None)
# print(df)
dfT = df.transpose()
# print(dfT)
# print(dfT.columns)
dfT.columns = ['kategoria hotelu', 'rok', 'ilosc']
# print(dfT['kategoria hotelu'].unique())
df1 = dfT[dfT['rok'] == '2015']
bars = df1['kategoria hotelu'].values
width = df1['ilosc'].values
x_pos = np.arange(len(bars))

plt.bar(x_pos, width, color=['black', 'blue', 'olive', 'yellow', 'green'])
plt.xticks(x_pos, bars, rotation=45)
plt.title('hotele w 2015')
plt.xlabel('kategoria hotelu')
plt.ylabel('liczba hoteli')

plt.tight_layout()
# dodaje padding na dole

plt.show()