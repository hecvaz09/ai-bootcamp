import csv

with open("servers.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)
    print()

    for row in reader:
        print("Server row:", row)
