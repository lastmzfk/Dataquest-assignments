## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')
wnba.head()
parameter = wnba['Games Played'].max()
sample = wnba['Games Played'].sample(random_state = 1)
statistic = sample.max()
sampling_error = parameter - statistic


## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')
sample_list = []
population_mean = wnba['PTS'].mean()
for i in range(100):
    sample = wnba['PTS'].sample(10, random_state = i)
    sample_list.append(sample.mean())

plt.scatter(range(1, 101), sample_list)
plt.axhline(population_mean)
plt.show()

## 7. Stratified Sampling ##

wnba['avg_scores_per_game'] = wnba['PTS'] / wnba['Games Played']
abb_list = ['F', 'G', 'C', 'G/F', 'F/C']
strats = []
for i in abb_list:
    strata = wnba[wnba['Pos'] == i]    
    strats.append([strata, i])
points_per_position = {}
for stratum, position in strats:
    sample = stratum['avg_scores_per_game'].sample(10, random_state = 0)
    points_per_position[position] = sample.mean()

position_most_points = max(points_per_position, key = points_per_position.get)
                                                   
    
        
        

## 8. Proportional Stratified Sampling ##

s_less = wnba[wnba['Games Played'] <= 12]
s_avg = wnba[(wnba['Games Played'] <= 22) & (wnba['Games Played'] > 12)]
s_max = wnba[wnba['Games Played'] > 22]
samples = []
for i in range(100):
    a = s_less.sample(1, random_state=i)
    b = s_avg.sample(2, random_state = i)
    c = s_max.sample(7, random_state = i)
    sample = pd.concat([a, b, c])
    samples.append(sample['PTS'].mean())
plt.scatter(range(1, 101), samples)
plt.axhline(wnba['PTS'].mean())
plt.show()
    

## 10. Cluster Sampling ##

clusters = pd.Series(wnba['Team'].unique()).sample(4, random_state = 0)

sample = pd.DataFrame()

for cluster in clusters:
    data_collected = wnba[wnba["Team"] == cluster]
    sample = sample.append(data_collected)
    
sampling_error_height = wnba['Height'].mean() - sample['Height'].mean()
sampling_error_age = wnba['Age'].mean() - sample['Age'].mean()
sampling_error_BMI = wnba['BMI'].mean() - sample['BMI'].mean()
sampling_error_points = wnba['PTS'].mean() - sample['PTS'].mean()
                      