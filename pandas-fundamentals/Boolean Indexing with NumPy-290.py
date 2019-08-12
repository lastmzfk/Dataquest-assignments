## 1. Reading CSV files with NumPy ##

import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',')
taxi_shape = taxi.shape

## 2. Reading CSV files with NumPy Continued ##

import numpy as np

taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',', skip_header = 1)
taxi_shape = taxi.shape


## 3. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])
a_bool = a < 3
b_bool = b == 'blue'
c_bool = c > 100

## 4. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]
print(february_bool)
print(february_rides)
print(february.shape)
print(february.shape[0])


## 5. Boolean Indexing with 2D ndarrays ##

tip_amount = taxi[:,12]
tip_bool = tip_amount > 50
top_tips = taxi[tip_bool, 5:14]

## 6. Assigning Values in ndarrays ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()
taxi_modified[28214, 5] = 1
taxi_modified[:, 0] = 16
boom = taxi_modified[1800:1802, 7]
baam = taxi_modified[:, 7].mean()
print(boom, baam)
taxi_modified[1800:1802, 7] = taxi_modified[:, 7].mean()


## 7. Assignment Using Boolean Arrays ##

# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()
total_amount = taxi_copy[:, 13]
total_amount[total_amount < 0] = 0

## 8. Assignment Using Boolean Arrays Continued ##

# create a new column filled with `0`.
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)
jfk_bool = taxi_modified[:, 5] == 2
lagurad_bool = taxi_modified[:, 5] == 3
newark_bool = taxi_modified[:, 5] == 5
taxi_modified[jfk_bool, 15] = 1
taxi_modified[newark_bool, 15] = 1
taxi_modified[lagurad_bool, 15] = 1



## 9. Challenge: Which is the most popular airport? ##

jfk = taxi[:,6] == 2
jfk_format = taxi[jfk, 6]
print(jfk_format)
print(jfk_format.shape)
jfk_count = taxi[jfk, 6].shape[0]
laguardia = taxi[:,6] == 3
laguardia_count = taxi[laguardia, 6].shape[0]
newark = taxi[:,6] == 5
newark_count = taxi[newark, 6].shape[0]


## 10. Challenge: Calculating Statistics for Trips on Clean Data ##

trip_mph = taxi[:,7] / (taxi[:,8] / 3600)
cleaned_taxi = taxi[trip_mph < 100]
mean_distance = cleaned_taxi[:, 7].mean()
mean_length = cleaned_taxi[:, 8].mean()
mean_total_amount = cleaned_taxi[:, 13].mean()

