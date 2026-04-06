import csv

with open("servers.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
