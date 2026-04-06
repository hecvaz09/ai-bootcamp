import requests


response = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
data = response.json()


print("Task Summery")
print("User ID:", data["userId"])
print("Task ID:", data["id"])
print("Title:", data["title"])


if data["completed"] == True:
    print("Status: Completed")
else:
    print("Status: Open")
