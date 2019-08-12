## 1. The JSON Format ##

world_cup_str = """
[
    {
        "team_1": "France",
        "team_2": "Croatia",
        "game_type": "Final",
        "score" : [4, 2]
    },
    {
        "team_1": "Belgium",
        "team_2": "England",
        "game_type": "3rd/4th Playoff",
        "score" : [2, 0]
    }
]
"""

import json 

world_cup_obj = json.loads(world_cup_str)

## 2. Reading a JSON file ##

file = open('hn_2014.json')
hn = json.load(file)

## 4. Writing List Comprehensions ##

# LOOP VERSION
#
# hn_clean = []
#
# for d in hn:
#     new_d = del_key(d, 'createdAtI')
#     hn_clean.append(new_d)

hn_clean = [del_key(dic, 'createdAtI') for dic in hn]


## 5. Using List Comprehensions to Transform and Create Lists ##

urls = [d['url'] for d in hn_clean]

## 6. Using List Comprehensions to Reduce a List ##

thousand_points = [d for d in hn_clean if d['points'] > 1000]
num_thousand_points = len(thousand_points)

## 7. Passing Functions as Arguments ##

def key_func(dic):
    value = dic['numComments']
    return value

most_comments = max(hn_clean, key=key_func)


## 8. Lambda Functions ##

# def multiply(a, b):
#    return a * b

multiply = lambda a, b: a * b

## 9. Using Lambda Functions to Analyze JSON data ##

hn_sorted_points = sorted(hn_clean, key = lambda d: d['points'], reverse = True)
top_5_titles = [d['title'] for d in hn_sorted_points[:5]]

## 10. Reading JSON files into pandas ##

import pandas as pd

hn_df = pd.DataFrame(hn_clean)

## 11. Exploring Tags Using the Apply Function ##

tags = hn_df['tags']

four_tags = tags[tags.apply(len) == 4]

## 12. Extracting Tags Using Apply with a Lambda Function ##

# def extract_tag(l):
#     return l[-1] if len(l) == 4 else None
cleaned_tags = tags.apply(lambda l: l[-1] if len(l) == 4 else None)

hn_df['tags'] = cleaned_tags