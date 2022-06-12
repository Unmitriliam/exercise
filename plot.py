import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

s = 1/10
x = np.arange(-5, 10, s)
a = np.sin(x)
b = np.cos(x)
y = a/b

plt.plot(x, y)
plt.subplots_adjust(hspace=0.5)

plt.show()



fig, ax = plt.subplots()

x1 = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec']
y1 = [21, 35, 42, 75, 68, 50]
y2 = [21, 31, 28, 27, 55, 70]
ax.plot(x1, y2, label='Filmy', linestyle='--', color='red')
ax.plot(x1, y1, label='Gry', linestyle='-', color='green')
ax.set_xlabel('miesiąc')
ax.set_ylabel('zyski')
ax.set_title('Zarobki')
ax.legend()
#ax.set_ylim(0,100)
ax.set_yticks(np.arange(0,101,step=20))
ax.set_xticks(np.arange(0,6, step=1), ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec'])
plt.show()
