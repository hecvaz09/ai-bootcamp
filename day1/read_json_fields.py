import json


with open("profile.json", "r") as file:
    data = json.load(file)


print("First skill:", data["skills"][0])
print("Second skill:", data["skills"][1])
print("Third skill:", data["skills"][2])
