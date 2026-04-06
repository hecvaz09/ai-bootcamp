import csv


total_hours = 0
day_count = 0


with open("study_data.csv", "r") as file:
    reader = csv.DictReader(file)


    for row in reader:
        day_count = day_count + 1
        total_hours = total_hours + int(row["hours"])


average_hours = total_hours / day_count


print("Study Report")
print("Days tracked:", day_count)
print("Total hours:", total_hours)
print("Average hours:", average_hours)


if total_hours >= 40:
    print("Excellent week.")
elif total_hours >= 30:
    print("Great start.")
else:
    print("Keep pushing.")
