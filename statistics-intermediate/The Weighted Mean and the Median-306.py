## 1. Introduction ##

mean_new = houses_per_year['Mean Price'].mean()
mean_original = houses['SalePrice'].mean()
difference = mean_original - mean_new

## 2. Different Weights ##

houses_per_year['total_sold'] = houses_per_year['Mean Price'] * houses_per_year['Houses Sold']
weighted_mean = houses_per_year['total_sold'].sum() / houses_per_year['Houses Sold'].sum()

mean_original = houses['SalePrice'].mean()
difference = mean_original - weighted_mean

## 3. The Weighted Mean ##

import numpy as np

def weighted_mean(x, y):
    total = x * y
    mean = sum(total)/sum(y)
    return mean

weighted_mean_function = weighted_mean(houses_per_year['Mean Price'], houses_per_year['Houses Sold'])

weighted_mean_numpy = np.average(a=houses_per_year['Mean Price'], weights = houses_per_year['Houses Sold'])
equal = (weighted_mean_numpy == weighted_mean_function)

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']

def median(x):
    x.sort(reverse = True)
    return x[int(len(x)/2 - 1.5)]

median1 = 23
median2 = 55
median3 = 32


## 5. Distributions with Even Number of Values ##

rooms = houses.copy()
rooms = rooms['TotRms AbvGrd'].replace({'10 or more': '10'}).astype(int).sort_values()

middle_indices = [int((len(rooms) / 2) - 1),
                  int((len(rooms) / 2))
                 ]
middle_values = rooms.iloc[middle_indices]
median = middle_values.mean()


## 6. The Median as a Resistant Statistic ##

import matplotlib.pyplot as plt

houses['Lot Area'].plot.box()
plt.show()
houses['SalePrice'].plot.box()
plt.show()
la_median = houses['Lot Area'].median()
la_mean = houses['Lot Area'].mean()
sp_median = houses['SalePrice'].median()
sp_mean = houses['SalePrice'].mean()
lotarea_difference = la_mean - la_median
saleprice_difference = sp_mean - sp_median


## 7. The Median for Ordinal Scales ##

mean = houses['Overall Cond'].mean()
median = houses['Overall Cond'].median()
houses['Overall Cond'].plot.hist()
more_representative = 'mean'