def read_lines(filename):
    with open(filename, "r") as file:
        return file.readlines()

def count_log_types(lines):
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

    return error_count, warning_count, info_count

def print_summary(errors, warnings, infos):
    print("Log Summary")
    print("Errors:", errors)
    print("Warnings:", warnings)
    print("Info messages:", infos)

lines = read_lines("system_log.txt")
errors, warnings, infos = count_log_types(lines)
print_summary(errors, warnings, infos)
