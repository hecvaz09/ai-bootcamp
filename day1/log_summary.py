file = open("system_log.txt", "r")
lines = file.readlines()
file.close()

error_count = 0
warning_count = 0
info_count = 0

for line in lines:
    if "ERROR" in line:
        error_count = error_count + 1
    elif "WARNING" in line:
        warning_count = warning_count + 1
    elif "INFO" in line:
        info_count = info_count + 1

print("Log Summary")
print("Errors:", error_count)
print("Warnings:", warning_count)
print("Info messages:", info_count)
