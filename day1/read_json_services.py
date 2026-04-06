import json

with open("device.json", "r") as file:
    data = json.load(file)

print("Services running:")

for service in data["services"]:
    print("-", service)
