import requests


response = requests.get("https://jsonplaceholder.typicode.com/todos/1")


with open("real_api_response.json", "w") as file:
    file.write(response.text)


print("real_api_response.json was created.")
