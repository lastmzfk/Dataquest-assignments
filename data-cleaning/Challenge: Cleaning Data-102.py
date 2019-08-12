## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()

true_avengers = avengers[avengers['Year'] > 1960]

## 5. Consolidating Deaths ##

def clean_deaths(row):
    death_list = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']

    num_deaths = 0

    for c in death_list:
        death = row[c]
        if pd.isnull(death) or death == 'NO':
            continue
        else:
            num_deaths += 1
    return num_deaths

true_avengers['Deaths'] = true_avengers.apply(clean_deaths, axis = 1)

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()
correct_joined_years = true_avengers[(2015 - true_avengers['Year']) == true_avengers['Years since joining']]
joined_accuracy_count = len(correct_joined_years)