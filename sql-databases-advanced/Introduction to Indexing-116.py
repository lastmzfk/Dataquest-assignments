## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")
schema = conn.execute("pragma table_info(facts);").fetchall()
for s in schema:
    print(s)

## 3. Explain query plan ##

query_plan_one = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE area > 40000;").fetchall()
query_plan_two = conn.execute("EXPLAIN QUERY PLAN SELECT area FROM facts WHERE area > 40000;").fetchall()
query_plan_three = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts where name = 'Czech Republic';").fetchall()
print(query_plan_one)
print(query_plan_two)
print(query_plan_three)

## 5. Time complexity ##

query_plan_four = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE id=20;").fetchall()
print(query_plan_four)

## 9. All together now ##

query_plan_six = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 10000;").fetchall()
print(query_plan_six)
conn.execute("create index if not exists pop_idx on facts(population);")
query_plan_seven = conn.execute("explain query plan select * from facts where population > 10000;").fetchall()
print(query_plan_seven)