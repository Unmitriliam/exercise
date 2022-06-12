import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('automobile.csv', header=0, sep=';', decimal='.')

print(df['Car model'])
print('------------------------------')
print(df)                   # Wyświetla ramkę danych
print(df.head())            # Wyświetla 5 pierwszych rekordów
print(df.tail(10))          # Wyświetla 10 ostatnich rekordów
print(df.columns)
print(df['Car model'][0:3])
print(df[['Car model', 'Fuel-type']][0:5])
print(df.iloc[2,3])         # Wyświetla konkretną pozycję jak tablica
print('------------------------------')

df2 = df[(df['Fuel-type'] == 'diesel')]             # Nowa ramka danych - Tylko rekordy 'Fuel-type' == 'diesel'
print(df2)                                          # Wyświetla nową ramkę danych
print(len(df2))                                     # Wyświetla długość nowej ramki danych
print(df2.sort_values('Horsepower', ascending=True))
print('------------------------------')

i = list(df2.groupby('Fuel-type').size())           # Wyświetla ilość
print(i)
print('------------------------------')

df3 = df.groupby('Fuel-type').count()                # .sum() sumuje liczbowe rekoedy , .count() liczy rekordy, .size() - liczy rekordy dla tej kolumny
print(df3)
ii = df['Fuel-type'].values
print(ii)
plt.show()

df2.to_csv('automobile-diesel.csv')                 # Zapisanie nowej ramki danych do pliku csv