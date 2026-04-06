import requests


try:
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
    print("Status code:", response.status_code)


    if response.status_code == 200:
       data = response.json()
       print("Request worked.")
       print("Title:", data["title"])
    else:
       print("Request failed with status code:", response.status_code)


except request.exeception.RequestException as e:
    print("Request error:", e)
