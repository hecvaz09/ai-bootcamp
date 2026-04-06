import json

device = {
    "hostname": "web2",
    "ip": "192.168.1.60",
    "status": "down",
    "cpu_usage": 92,
    "services": ["http", "ssh"]
}

with open("new_device.json", "w") as file:
    json.dump(device, file, indent=2)

print("new_device.json was created.")
