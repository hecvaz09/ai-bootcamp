import requests


response = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
data = response.json()


report_text = ""
report_text = report_text + "Task Summary\n"
report_text = report_text + "User ID: " + str(data["userId"]) + "\n"
report_text = report_text + "Task ID: " + str(data["id"]) + "\n"
report_text = report_text + "Title: " + data["title"] + "\n" 


if data["completed"] == True:
    report_text = report_text + "Status: Completed\n"
else:
    report_text = report_text + "Status: Open\n"


with open("Task_summary.txt", "w") as file:
     file.write(report_text)


print("task_summary.text was created.")
