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
    while True:
        try:
            priority = int(input("What is the priority of this task from 1-10 (1 = most important): "))
            if 1 <= priority <= 10:
                break
            else:
                print("Priority must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid integer.")
    task_id = max([task["id"] for task in tasks], default=0) + 1
    task = {"id": task_id, "title": title, "deadline": deadline, "status": status, "priority":priority}
    tasks.append(task)
    tasks.sort(key=lambda t: (t['priority'],datetime.strptime(t['deadline'], "%d-%m-%Y")))
    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
    print("Task was succesfully added!")
def viewtasks():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as f:
            dane = json.load(f)
        if not dane:
            print("Brak zadań.")
            return
        dane.sort(key=lambda t: (t['priority'], datetime.strptime(t['deadline'], "%d-%m-%Y")))
        for task in dane:
            print(f"ID: {task['id']} | Tytuł: {task['title']} | Termin: {task['deadline']} | Status: {task['status']} | Priorytet: {task['priority']}")
    except FileNotFoundError:
        print("No file found")

    
def updatetask():
    pass