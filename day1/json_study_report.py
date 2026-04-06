import json


with open("study_profile.json", "r") as file:
    data = json.load(file)


total = 0


for hours in data["study_hours"]:
    total = total + hours


average = total / len(data["study_hours"])


print("Study Report")
print("Name:", data["name"])
print("Goal:", data["goal"])
print("Total hours;", total)
print("Average hours", average)


if total >= 40:
    print("Excellent week.")
elif total >= 30:
    print("Great start.")
else:
    print("Keep pushing.")
