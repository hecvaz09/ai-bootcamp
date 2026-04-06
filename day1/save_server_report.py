import csv

down_count = 0
high_cpu_count = 0
healthy_count = 0

report_lines = []

with open("servers.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        hostname = row["hostname"]
        ip = row["ip"]
        status = row["status"]
        cpu_usage = int(row["cpu_usage"])

        if status == "down":
            result = "DOWN"
            down_count = down_count + 1
        elif cpu_usage > 85:
            result = "HIGH CPU"
            high_cpu_count = high_cpu_count + 1
        else:
            result = "HEALTHY"
            healthy_count = healthy_count + 1

        line = f"{hostname} ({ip}) -> {result}"
        report_lines.append(line)

summary = []
summary.append("----- SERVER REPORT -----")
summary.extend(report_lines)
summary.append("")
summary.append("----- SUMMARY -----")
summary.append(f"Down servers: {down_count}")
summary.append(f"High CPU servers: {high_cpu_count}")
summary.append(f"Healthy servers: {healthy_count}")

with open("server_report.txt", "w") as file:
    for line in summary:
        file.write(line + "\n")

print("server_report.txt was created.")
