## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan
f500_selection = f500.loc[:, ['rank', 'revenues', 'revenue_change']].head()


## 2. Reading CSV files with pandas ##

import numpy as np
import pandas as pd

f500 = pd.read_csv('f500.csv')
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 3. Using iloc to select by integer position ##

fifth_row = f500.iloc[4]
company_value = f500.iloc[0, 0]

## 4. Using iloc to select by integer position continued ##

first_three_rows = f500.iloc[:3]
first_seventh_row_slice = f500.iloc[[0, 6], :5]


## 5. Using pandas methods to create boolean masks ##

boolean = f500['previous_rank'].isnull()
null_previous_rank = f500.loc[boolean, ['company', 'rank', 'previous_rank']]

## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]
top5_null_prev_rank = null_previous_rank.iloc[:5]

## 7. Pandas Index Alignment ##

rank_bool = f500['previous_rank'].notnull()
previously_ranked = f500.loc[rank_bool]
rank_change = previously_ranked['previous_rank'] - previously_ranked['rank']
f500['rank_change'] = rank_change

## 8. Using Boolean Operators ##

revenue_bool = f500['revenues'] > 100000
profits_bool = f500['profits'] < 0
large_revenue = f500[revenue_bool]
negative_profits = f500[profits_bool]
combined = f500[revenue_bool & profits_bool]
big_rev_neg_profit = combined

## 9. Using Boolean Operators Continued ##

brazil_venezuela = f500[(f500['country'] == 'Brazil') | (f500['country'] == 'Venezuela')]
tech_outside_usa = f500[(f500['sector'] == 'Technology') & ~(f500['country'] == 'USA')].head()

## 10. Sorting Values ##

japan = f500[f500['country'] == 'Japan'].sort_values('employees', ascending = False)
top_japanese_employer = japan.iloc[0,0]




## 11. Using Loops with pandas ##

top_employer_by_country = {}

countries = f500['country'].unique()


for c in countries:
    top_employers = f500[f500['country'] == c].sort_values('employees',ascending = False)
    top_employer = top_employers.iloc[0,0]
    top_employer_by_country[c] = top_employer

## 12. Challenge: Calculating Return on Assets by Country ##

return_on_assets = f500['profits'] / f500['assets']
f500['roa'] = return_on_assets

top_roa_by_sector = {}

sectors = f500['sector'].unique()

for c in sectors:
    sec_companies = f500[f500['sector'] == c].sort_values('roa', ascending = False)
    sec_company = sec_companies.iloc[0,0]
    top_roa_by_sector[c] = sec_company
    