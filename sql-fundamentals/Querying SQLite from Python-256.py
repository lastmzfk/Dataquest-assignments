## 3. Connecting to the Database ##

import sqlite3

conn = sqlite3.connect('jobs.db')

## 6. Creating a Cursor and Running a Query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])
query_1 = "SELECT Major FROM recent_grads"
cursor.execute(query_1)
majors = cursor.fetchall()
print(majors[0:2])

## 8. Fetching a Specific Number of Results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
query = "select Major, Major_category from recent_grads"
fetch = cursor.execute(query)
five_results = cursor.fetchmany(5)
print(five_results)

## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

jobs2 = sqlite3.connect('jobs2.db')
cursor = jobs2.cursor()
query = "SELECT Major FROM recent_grads ORDER BY Major DESC"
fetch = cursor.execute(query)
reverse_alphabetical = cursor.fetchall()
jobs2.close()
