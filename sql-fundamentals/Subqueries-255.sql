## 2. Subqueries ##

select Major, Unemployment_rate from recent_grads
where Unemployment_rate < 
(select AVG(Unemployment_rate) from recent_grads)
order by Unemployment_rate

## 3. Subquery In SELECT ##

SELECT CAST(COUNT(*) as float) / (SELECT CAST(COUNT(*) as float) FROM recent_grads)  AS proportion_abv_avg FROM recent_grads
WHERE ShareWomen >
(SELECT AVG(ShareWomen) FROM recent_grads)


## 4. Returning Multiple Results In Subqueries ##

SELECT Major, Major_category FROM recent_grads
WHERE Major_category IN (select Major_category from recent_grads
GROUP BY Major_category
ORDER BY SUM(Total) DESC
LIMIT 5)


## 5. Building Complex Subqueries ##

SELECT AVG(cast(Sample_size as float)/cast(Total as float)) AS avg_ratio FROM recent_grads

## 6. Practice Integrating A Subquery With The Outer Query ##

SELECT Major, Major_category, cast(Sample_size as float)/cast(Total as float) AS ratio FROM recent_grads
WHERE Ratio >
(select AVG(cast(Sample_size as float)/cast(Total as float)) FROM recent_grads)
