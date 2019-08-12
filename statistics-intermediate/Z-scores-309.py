## 1. Individual Values ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

import matplotlib.pyplot as plt

houses['SalePrice'].plot.kde(xlim = (houses['SalePrice'].min(), houses['SalePrice'].max()))
mean = houses['SalePrice'].mean()
plt.axvline(mean, color = 'black', label = 'Mean')
sd = houses['SalePrice'].mean() + houses['SalePrice'].std(ddof = 0)
plt.axvline(sd, label = 'Standard deviation', color = 'red')
plt.axvline(220000, label = '220000', color = 'orange')
plt.legend()

very_expensive = False





## 2. Number of Standard Deviations ##

dist = 220000 - houses['SalePrice'].mean()
st_devs_away = dist/houses['SalePrice'].std(ddof = 0)


## 3. Z-scores ##

min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

def z_score(v, x):
    mean = x.mean()
    std = x.std(ddof = 0)
    return (v - mean) / std

min_z = z_score(min_val, houses['SalePrice'])
mean_z = z_score(mean_val, houses['SalePrice'])
max_z = z_score(max_val, houses['SalePrice'])

                
    

## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z

z_regions = {}
regions = ['NAmes', 'CollgCr', 'OldTown', 'Edwards', 'Somerst']

for region in regions:
    temp_houses = houses[houses['Neighborhood'] == region].copy()
    temp_string = temp_houses['SalePrice']
    z_regions[region] = z_score(200000, temp_string, bessel = 0)
    
best_investment = "College Creek"

## 5. Transforming Distributions ##

mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
houses['z_prices'] = houses['SalePrice'].apply(
    lambda x: ((x - mean) / st_dev)
    )

z_mean_price = houses['z_prices'].mean()
z_stdev_price = houses['z_prices'].std(ddof = 0)

mean_area = houses['Lot Area'].mean()
stdev_area = houses['Lot Area'].std(ddof = 0)
houses['z_area'] = houses['Lot Area'].apply(lambda x: ((x - mean_area) / stdev_area))

z_mean_area = houses['z_area'].mean()
z_stdev_area = houses['z_area'].std(ddof = 0)

## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]
p_mean = mean(population)
p_std = std(population, ddof = 0)
pop_z = []
for i in population:
    z_score = (i - p_mean) / p_std
    pop_z.append(z_score)
mean_z = mean(pop_z)
stdev_z = std(pop_z, ddof = 0)




## 7. Standardizing Samples ##

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
    
stdev_sample = std(standardized_sample, ddof = 1)


## 8. Using Standardization for Comparisons ##

def stand_dist(x):
    mean = x.mean()
    std = x.std(ddof=0)
    standardized = []
    for i in x:
        z = (i - mean) / std
        standardized.append(z)
    return standardized

houses['z_1'] = stand_dist(houses['index_1'])
houses['z_2'] = stand_dist(houses['index_2'])

print(houses['z_1'].head(2))
print(houses['z_2'].head(2))
better = 'first'



## 9. Converting Back from Z-scores ##

houses['new_dist'] = houses['z_merged'] * 10 + 50
mean_transformed = houses['new_dist'].mean()
stdev_transformed = houses['new_dist'].std(ddof = 0)
