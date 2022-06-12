import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

names = ['chomiki', 'psy', 'koty', 'jaszczurki']
prt = [71.5, 11, 5.5, 12]

colors = ['red', 'blue', 'yellow', 'pink']

plt.pie(prt,
        labels=names,               # Nazwy kawałków
        colors=colors,              # Kolory
        shadow=True,                # Cień
        explode=(0, 0.1, 0, 0.2),   # Wysunięcie konkretnych części
        autopct='%1.2f%%',           # Pokazanie procentów oraz format miejsc po przecinku
        wedgeprops={'edgecolor': 'black'},          # Obwódka
        textprops={'fontsize': 14}                  # Czcionka tekstu
        )

plt.title('Zwierzęta')
plt.legend()
plt.show()
