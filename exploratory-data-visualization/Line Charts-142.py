## 2. Introduction To The Data ##

import pandas as pd

unrate = pd.read_csv('unrate.csv')

unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt

plt.plot()
plt.show()

## 7. Adding Data ##

first_twelve = unrate[:12]
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.show


## 8. Fixing Axis Ticks ##

frsttwlv = unrate[:12]
plt.plot(frsttwlv['DATE'], frsttwlv['VALUE'])
plt.xticks(rotation = 90)
plt.show()

## 9. Adding Axis Labels And A Title ##

ftw = unrate[:12]
plt.plot(ftw['DATE'], ftw['VALUE'])
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.xticks(rotation = 90)