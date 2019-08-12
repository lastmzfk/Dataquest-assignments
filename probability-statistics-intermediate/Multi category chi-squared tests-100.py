## 2. Calculating expected values ##

males_over50k = 32561 * .241 * .67
males_under50k = 32561 * (1 - .241) * .67
females_over50k = 32561 * .241 * .33
females_under50k = 32561 * (1 - .241) * .33

## 3. Calculating chi-squared ##

males_over50k = 32561 * .241 * .67
males_under50k = 32561 * (1 - .241) * .67
females_over50k = 32561 * .241 * .33
females_under50k = 32561 * (1 - .241) * .33

def chisq(obs, exp):
    return (obs - exp) ** 2 / exp

mo50k = chisq(6662, males_over50k)
mu50k = chisq(15128, males_under50k)
fo50k = chisq(1179, females_over50k)
fu50k = chisq(9592, females_under50k)
chisq_gender_income = mo50k + fo50k + mu50k + fu50k


## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare

observed = np.array([6662, 1179, 15128, 9592])
expected = np.array([5257.6, 2589.6, 16558.2, 8155.6])

chisquare_value, pvalue_gender_income = chisquare(observed, expected)

## 5. Cross tables ##

import pandas as pd

table = pd.crosstab(income['sex'], [income['race']])
print(table)

## 6. Finding expected values ##

import scipy
pvalue_gender_race = scipy.stats.chi2_contingency(table)[1]