import json


with open("api_response.json", "r") as file:
     data = json.load(file)


print("Status:", data["status"])
print("Server:", data["server"])
print("Errors:", data["errors"])
print("Warnings:", data["warnings"])
print("Uptime hours:", data["uptime hours"])


if data["errors"] > 0:
    print("Server needs attention.")
else:
    print("Server looks good.")
