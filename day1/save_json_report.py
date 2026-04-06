import json


with open("study_profile.json", "r") as file:
    data = json.load(file)


total = 0


for hours in data["study_hours"]:
    total = total + hours


average = total / len(data["study_hours"])


report_text = ""
report_text = report_text + "Study Report\n"
report_text = report_text + "Name: " + data["name"] + "\n"
report_text = report_text + "Goal: " + data["goal"] + "\n"
report_text = report_text + "Total hours: " + str(total) + "\n"
report_text = report_text + "Average hours: " + str(average) + "\n"


if total >= 40:
    report_text = report_text + "Excellent week.\n"
elif total >= 30:
    report_text = report_text + "Great start.\n"
else: 
    report_text = report_text + "keep pushing.\n"


with open("json_study_report.txt", "w") as file:
    file.write(report_text)


print("json_study_report.txt was created.")
