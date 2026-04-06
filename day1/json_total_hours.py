import json


with open("study_profile.json", "r") as file:
    data = json.load(file)


total = 0


for hours in data["study_hours"]:
    total = total + hours


print("Name:", data["name"])
print("Goal:", data["goal"])
print("Study:", data["study_hours"])
print("Total hours:", total)
