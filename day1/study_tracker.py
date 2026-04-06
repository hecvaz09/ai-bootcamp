days = int(input("How many days will you study? "))
hours_per_day = float(input("How many hours per day? "))

total = days * hours_per_day

print("Total study hours:", total)

if total >= 240:
    print("Excellent job.")
else:
    print("Keep going. You need more study hours.")
