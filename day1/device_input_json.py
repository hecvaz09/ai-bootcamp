import json

hostname = input("Enter hostname: ")
ip = input("Enter IP address: ")
status = input("Enter status: ")
cpu_usage = int(input("Enter CPU usage: "))

device = {
    "hostname": hostname,
    "ip": ip,
    "status": status,
    "cpu_usage": cpu_usage
}

with open("user_device.json", "w") as file:
    json.dump(device, file, indent=2)

print("user_device.json was created.")
