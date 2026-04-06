file = open("system_log.txt", "r")
lines = file.readlines()
file.close()

print("Error lines:")

for line in lines:
    if "ERROR" in line:
        print(line.strip())
