import csv

with open("study_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Day:", row["day"])
        print("Hours:", row["hours"])
        print("Topic:", row["topic"])
