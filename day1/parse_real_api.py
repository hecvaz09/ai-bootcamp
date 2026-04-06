import requests


response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = response.json()


print("User ID:", data["userId"])
print("Task ID:", data["id"])
print("Title:", data["title"])
print("Completed:", data["completed"])


if data["completed"] == True:
    print("Task is completed.")
else:
    print("Task is not completed.")
