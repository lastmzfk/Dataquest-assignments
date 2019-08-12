## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

def difference(x):
    return(max(x) - min(x))

range_by_year = {}
years = houses['Yr Sold'].unique()
for year in years:
    houses_year = houses[houses['Yr Sold'] == year].copy()
    range_by_year[year] = difference(houses_year['SalePrice'])
one = False
two = True

           


## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]

def var(x):
    mean = sum(x)/len(x)
    dev = []
    for i in x:
        a = i - mean
        dev.append(a)
    return sum(dev)/len(dev)

avg_distance = var(C)

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]

def av_abs_dev(x):
    mean = sum(x)/len(x)
    ans = []
    for i in x:
        deviation = abs(i-mean)
        ans.append(deviation)
    return sum(ans)/len(ans)

mad = av_abs_dev(C)


## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]

def variance(x):
    mean = sum(x)/len(x)
    l = []
    for i in x:
        var = (i - mean)**2
        l.append(var)
    return sum(l)/len(l)

variance_C = variance(C)

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

def standart_deviation(x):
    mean = sum(x)/len(x)
    l = []
    for i in x:
        var = (i - mean)**2
        l.append(var)
    return sqrt(sum(l)/len(l))

standard_deviation_C = standart_deviation(C)

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

years = houses['Yr Sold'].unique()
year_dict = {}
for year in years:
    price = houses[houses['Yr Sold'] == year]
    year_dict[year] = standard_deviation(price['SalePrice'])

lowest_variability = 2010
greatest_variability = 2006

## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

bigger_spread = 'sample 2'
st_dev1 = standart_deviation(sample1)
st_dev2 = standart_deviation(sample2)

## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt

sample_list = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    sample_list.append(standart_deviation(sample))

plt.hist(sample_list)
plt.axvline(standart_deviation(houses['SalePrice']))
plt.show()

## 9. Bessel's Correction ##

from math import sqrt
def population_standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

from math import sqrt
def sample_standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / (len(distances)-1)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = sample_standard_deviation(sample)
    st_devs.append(st_dev)

pop_stdev = population_standard_deviation(houses['SalePrice'])
plt.hist(st_devs)
plt.axvline(pop_stdev)
plt.show()


## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var

pandas_stdev = sample['SalePrice'].std(ddof = 1)
numpy_stdev = std(sample['SalePrice'], ddof = 1)
equal_stdevs = (pandas_stdev == numpy_stdev)

pandas_var = sample['SalePrice'].var(ddof = 1)
numpy_var = var(sample
                ['SalePrice'], ddof = 1)
equal_vars = (pandas_var == numpy_var)




## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]
from numpy import var, std

pop_var = var(population, ddof = 0)
pop_std = std(population, ddof = 0)

st_devs = []
variances = []

for sample in samples:
    st_devs.append(std(sample, ddof = 1))
    variances.append(var(sample, ddof = 1))
    
mean_std = sum(st_devs) / len(st_devs)
mean_var = sum(variances) / len(variances)

equal_stdev = pop_std == mean_std
equal_var = pop_var == mean_var