import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pie chart z ramki danych z jednego roku, indeks lewy gorny rog

df = pd.read_excel('mieszkania2.xlsx')

# rozbicie ramki danych
df1 = df[df['Rok'] == 2015]
# 2015 to int dlatego == bez ''

labels = df1['Formy budownictwa']
sizes = df1['Wartość']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# plt.axis('equal')
plt.title('Rok 2015')

# plt.annotate('114899', xy=(-1, 1))
plt.text(-1, 1, '114899')
plt.show()