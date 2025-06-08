import json
import os
from datetime import datetime
from operator import itemgetter
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    return []
def addtask():
    tasks = load_tasks()
    title = input("Task name:")
    while True:
        deadline = input("What is the due date?(Put it in format dd-mm-rrrr)")
        try:
            deadline_date = datetime.strptime(deadline,"%d-%m-%Y")
            break
        except ValueError:
            print("You have entered wrong date format. Try again")
    while True:
        status = input("What is the status of this task?(Not started,In progress, Finished):")
        status_progress = ["Not started","In progress", "Finished"]
        try:
            if status in status_progress:
                break
        except:
            print("Wrong status, try again")
    task_id = max([task["id"] for task in tasks], default=0) + 1
    task = {"id": task_id, "title": title, "deadline": deadline, "status": status}
    tasks.append(task)
    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
        json.dumps(sorted(deadline, key=itemgetter('deadline')))
    print("Task was succesfully added!")
def viewtasks():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as f:
            dane = json.load(f)
        print(dane)
    except FileNotFoundError:
        print("No file found")
def updatetask():
    pass