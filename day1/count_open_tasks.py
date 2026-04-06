import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos", timeout=10)
data = response.json()

open_count = 0
completed_count = 0

for task in data[:20]:
    if task["completed"] == True:
        completed_count = completed_count + 1
    else:
        open_count = open_count + 1

print("First 20 tasks summary")
print("Completed tasks:", completed_count)
print("Open tasks:", open_count)
