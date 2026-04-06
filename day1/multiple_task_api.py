import requests 


response = requests.get("https://jsonplaceholder.typicode.com/todos", timeout=10)
data = response.json()


print("First 5 tasks:") 
print()


for task in data[:5]:
    print("Task ID:", task["id"])
    print("Title:", task["title"])
    print("Completed:", task["completed"])
    print("---")
