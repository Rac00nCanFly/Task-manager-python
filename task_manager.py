import json
import os
from datetime import datetime
from operator import itemgetter
import math
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    return []
def addtask():
    tasks = load_tasks()
    title = input("Task name:")
    category = input("Category of the task:")
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
            if status == "Not started" or status == "In progress":
                break
            elif status == 'Finished':
                completed_at = input("When did you completed it?")
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
    created_at = datetime.now().isoformat()
    task = {"id": task_id,"category":category, "title": title, "deadline": deadline, "status": status, "priority":priority, "created_at":created_at}
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
            print(f"ID: {task['id']} | Category:{task['category']}| Tytuł: {task['title']} | Termin: {task['deadline']} | Status: {task['status']} | Priorytet: {task['priority']}")
    except FileNotFoundError:
        print("No file found")

def update_priority(tasks):
    today = datetime.now()
    for task in tasks:
        created_at = datetime.fromisoformat(task['created_at'])
        days_waiting = (today - created_at).days
        new_priority = min(max_priority, int(min_priority + K *math.log(days_waiting+1)))
    print(days_left)
def setting_parameters():
    max_days = input("What is the maximum number of days after which task should be completed?(e.g.: usually you input tasks in 14 days advance their deadline)")
    min_days = input("What is the minimum time after which the task should be marked as high priority?")
    max_priority = 100
    min_priority = 1
    K = (max_priority-min_priority)/(math.log(max_days+1))
def saving_history_for_ML():

def updatetask():
    if status == 'Finished':
        completion_time = input("How much time did it take to complete this task?(Input in hours)")