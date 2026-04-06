import requests
from requests.execptions import RequestException

url = "https://api.github.com"


try:
    response = requests.get(url, timeout=10)


    print("Status code:", response.status_code)
    print("Success:", response.ok)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Response.body:")
    print(response.text)


except RequestException as e:
    print("Request failed:", e)
