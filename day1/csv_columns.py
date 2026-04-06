import csv

with open("servers.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        hostname = row[0]
        ip = row[1]
        status = row[2]
        cpu_usage = row[3]

        print("Hostname:", hostname)
        print("IP:", ip)
        print("Status:", status)
        print("CPU usage:", cpu_usage)
        print("---")
