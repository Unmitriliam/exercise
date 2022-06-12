import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d = 1/7
x = np.arange(-2, 8, d)
a = np.sin(x)
b = np.cos(x)
c = x**3
y = (a+b)*c

plt.plot(x, y, 'r-')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('wykres f(x)')
plt.subplots_adjust(hspace=0.5)
plt.show()

df = pd.read_csv('flags.csv', header=0, sep=';', decimal='.')
print(df)

Katolicyzm = df[((df[ 'Religion'] == 'Catholic') )]
print(Katolicyzm)

i = list(Katolicyzm.groupby('Landmass').size())
# print(i)

grupa = Katolicyzm.groupby('Landmass')
etykiety = list(grupa.groups.keys())

plt.bar(x=etykiety, height=i, color=['red', 'green', 'blue', 'yellow'])
plt.xlabel('Kontynenty')
plt.ylabel('Ilość krajów')
plt.show()

# e = pd.plotting.table(ax=None, data=Katolicyzm, rowLabels=None, colLabels=None, kwargs=i)
# print(e)

rd = pd.read_csv('flags.csv', header=0, sep=';', decimal='.')

d = (df.groupby('Zone').agg({'Population': ['sum']}))
print(d)

# series = pd.Series(3 * np.random.rand(4), index=["a", "b", "c", "d"], name="series")
#
# series.plot.pie(figsize=(6, 6));