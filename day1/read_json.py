import json


with open("profile.json", "r") as file:
    data = json.load(file)


print("Name:", data["name"])
print("Goal:", data["goal"])
print("Hours per day:", data["hours_per_day"])
print("Skills:", data["skills"])
