## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]
center = False

mean = sum(distribution) / len(distribution)

above = []
below = []

for value in distribution:
    if value < mean:
        below.append(mean - value)
    if value > mean:
        above.append(abs(mean - value))

equal_distances = (sum(above) == sum(below))

    

## 3. The Mean as a Balance Point ##

from numpy.random import randint, seed
equal_distances = 0
for dist in range(5000):
    seed(dist)
    distribution = randint(0, 1000, 10)
    mean = sum(distribution) / len(distribution)
    above = []
    below = []
    for i in distribution:
        if i > mean:
            above.append(abs(mean - i))
        if i < mean:
            below.append(mean - i)
    sum_above = round(sum(above), 1)
    sum_below = round(sum(below), 1)
    if sum_above == sum_below:
        equal_distances += 1
    else:
        continue
print(equal_distances)
    

## 4. Defining the Mean Algebraically ##

one = False
two = False
three = False

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]
def mean(n):
    meow = 0
    for i in n:
        meow += i
    meoow = meow / len(n)
    return meoow
mean_1 = mean(distribution_1)
mean_2 = mean(distribution_2)
mean_3 = mean(distribution_3)

## 6. Introducing the Data ##

houses = pd.read_csv('AmesHousing_1.txt', sep='\t')
one = True
two = False
three = True


## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)

function_mean = mean(houses['SalePrice'])
pandas_mean = houses['SalePrice'].mean()
means_are_equal = (function_mean == pandas_mean)


## 8. Estimating the Population Mean ##

pop_mean = houses['SalePrice'].mean()

w = 5
sampling_errors = []
sample_size = []

for i in range(101):
    sample = houses['SalePrice'].sample(w, random_state = i)
    sample_size.append(w)
    w += 29
    sample_mean = pop_mean - sample.mean()
    sampling_errors.append(sample_mean)
    
import matplotlib.pyplot as plt
plt.scatter(sample_size, sampling_errors)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')
plt.show()



## 9. Estimates from Low-Sized Samples ##

population_mean = houses['SalePrice'].mean()

sample_means = []

for i in range(10000):
    sample = houses['SalePrice'].sample(100, random_state = i)
    s_mean = sample.mean()
    sample_means.append(s_mean)

plt.hist(sample_means)
plt.xlim(0, 500000)
plt.axvline(population_mean)
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.show()

## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]
samples = [[3,7], [3,2],[7,2], [7,3], [2,3],[2,7]]

sample_means = []
for sample in samples:
    sample_means.append(sum(sample) / 2)

sample_mean = sum(sample_means)/len(sample_means)
population_mean = sum(population)/len(population)
unbiased = (sample_mean == population_mean)