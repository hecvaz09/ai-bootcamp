import requests


response = requests.get("https://jsonplaceholder.typicode.com/todos/1")


print("Status code:", response.status_code)


if response.status_code == 200:
    data = response.json()


    print("API resquest worked.")
    print("Title:", data["title"])

    
    if data["completed"] == True:
       print("Task is completed.")
    else:
       print("Task is still open.")

else:
    print("API request failed.")
