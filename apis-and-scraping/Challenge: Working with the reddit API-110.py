## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers = headers, params = params)
python_top = response.json()


## 3. Getting the Most Upvoted Post ##

['python_top_articles = python_top["data"]["children"]\nmost_upvoted = ""\nmost_upvotes = 0\nfor article in python_top_articles:\n    ar = article["data"]\n    if ar["ups"] >= most_upvotes:\n        most_upvoted = ar["id"]\n        most_upvotes = ar["ups"]']

## 4. Getting Post Comments ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers = headers)
comments = response.json()

## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1]["data"]["children"]
most_upvoted_comment = ""
most_upvotes_comment = 0
for comment in comments_list:
    co = comment['data']
    if co['ups'] >= most_upvotes_comment:
        most_upvoted_comment = co['id']
        most_upvotes_comment = co['ups']

## 6. Upvoting a Comment ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
payload = {"dir": 1, "id": "d16y4ry"}
response = requests.post("https://oauth.reddit.com/api/vote", headers = headers, json = payload)
status = response.status_code