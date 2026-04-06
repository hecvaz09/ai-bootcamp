import csv


total_hours = 0


with open("study_data.csv", "r") as file: 
    reader = csv.DictReader(file)


    for row in reader:
        total_hours = total_hours + int(row["hours"])


print("Total study hours:", total_hours)
