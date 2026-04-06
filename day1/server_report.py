import csv

down_count = 0
high_cpu_count = 0
healthy_count = 0

with open("servers.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        hostname = row["hostname"]
        ip = row["ip"]
        status = row["status"]
        cpu_usage = int(row["cpu_usage"])

        print("Server:", hostname)
        print("IP:", ip)
        print("Status:", status)
        print("CPU:", cpu_usage)

        if status == "down":
            print("Result: DOWN")
            down_count = down_count + 1
        elif cpu_usage > 85:
            print("Result: HIGH CPU")
            high_cpu_count = high_cpu_count + 1
        else:
            print("Result: HEALTHY")
            healthy_count = healthy_count + 1

        print()

print("----- SUMMARY -----")
print("Down servers:", down_count)
print("High CPU servers:", high_cpu_count)
print("Healthy servers:", healthy_count)
