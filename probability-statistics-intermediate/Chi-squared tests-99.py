## 2. Calculating differences ##

male_diff = (21790 - 16280.5) / 16280.5
female_diff = (10771 - 16280.5) / 16280.5


## 3. Updating the formula ##

male_diff = (21790 - 16280.5) ** 2 / 16280.5
female_diff = (10771 - 16280.5) ** 2 / 16280.5
gender_chisq = male_diff + female_diff

## 4. Generating a distribution ##

from numpy.random import random
import matplotlib.pyplot as plt

chi_squared_values = []
for i in range(1000):
    sequence = random((32561,))
    sequence[sequence < .5] = 0
    sequence[sequence >= .5] = 1
    male_count = len(sequence[sequence == 0])
    female_count = len(sequence[sequence == 1])
    male_diff = (male_count - 16280.5) **2 / 16280.5
    female_diff = (female_count - 16280.5) ** 2 / 16280.5
    chi_squared = male_diff + female_diff
    chi_squared_values.append(chi_squared)
    
plt.hist(chi_squared_values)

            

## 6. Smaller samples ##

male_diff = (217.9 - 162.805) ** 2 / 162.805
female_diff = (107.71 - 162.805) ** 2 / 162.805
gender_chisq = male_diff + female_diff


## 7. Sampling distribution equality ##

chi_squared_values = []

from numpy.random import random
import matplotlib.pyplot as plt

for i in range(1000):
    vector = random((300,))
    vector[vector < .5] = 0
    vector[vector >= .5] = 1
    male_rand = len(vector[vector == 0])
    female_rand = len(vector[vector == 1])
    male_diff = (male_rand - 150) ** 2 / 150
    female_diff = (female_rand - 150) ** 2 / 150 
    chi_square = male_diff + female_diff
    chi_squared_values.append(chi_square)

plt.hist(chi_squared_values)    

## 9. Increasing degrees of freedom ##

categories = ['White',
              'Black',
              'Asian-Pac-Islander',
              'Amer-Indian-Eskimo',
              'Other'
             ]
diffs = []
observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

for i in range(5):
    chi_square = (observed[i] - expected[i]) ** 2 / expected[i]
    diffs.append(chi_square)

race_chisq = sum(diffs)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

diffs = []
observed = np.array([27816, 3124, 1039, 311, 271])
expected = np.array([26146.5, 3939.9, 944.3, 260.5, 1269.8])
chisquare_value, race_pvalue = chisquare(observed, expected)
