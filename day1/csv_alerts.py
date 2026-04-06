import csv

with open("servers.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        hostname = row[0]
        status = row[2]
        cpu_usage = int(row[3])

        print("Checking:", hostname)

        if status == "down":
            print("ALERT: server is down")
        elif cpu_usage > 85:
            print("WARNING: high CPU usage")
        else:
            print("Server looks okay")

        print()
