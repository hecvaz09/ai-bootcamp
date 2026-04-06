name = input("Enter your name: ")
goal = input("Enter your goal job: ")

days = []
total = 0

for i in range(5):
    hours = float(input("Enter study hours for day " + str(i + 1) + ": "))
    days.append(hours)
    total = total + hours

student = {
    "name": name,
    "goal": goal,
    "days": days,
    "total_hours": total
}

print()
print("----- STUDY SUMMARY -----")
print("Name:", student["name"])
print("Goal:", student["goal"])
print("Daily hours:", student["days"])
print("Total hours:", student["total_hours"])

if total >= 30:
    print("Great start.")
else:
    print("Keep pushing.")
