import json
import os
import csv
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
            priority = int(input("What is the priority of this task from 1-100 (100 = most important): "))
            if 1 <= priority <= 100:
                break
            else:
                print("Priority must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid integer.")
    task_id = max([task["id"] for task in tasks], default=0) + 1
    created_at = datetime.now().isoformat()
    task = {"id": task_id,"category":category, "title": title, "deadline": deadline, "status": status, "priority":priority, "user_priority": priority,"created_at":created_at}
    tasks.append(task)
    tasks.sort(key=lambda t: (t['priority'],datetime.strptime(t['deadline'], "%d-%m-%Y")))
    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
    print("Task was succesfully added!")
def viewtasks():
    try:
        with open('params.json', 'r') as f:
            params = json.load(f)
        min_priority = params['min_priority']
        max_priority = params['max_priority']
        K = params['K']
    except FileNotFoundError:
        print("Parameters not set. Please use 'Set parameters' first.")
        return
    try:
        with open('tasks.json', 'r', encoding='utf-8') as f:
            dane = json.load(f)
        if not dane:
            print("Brak zadań.")
            return
        update_priority(dane, min_priority, max_priority, K)
        dane.sort(key=lambda t: (t['priority'], datetime.strptime(t['deadline'], "%d-%m-%Y")))
        for task in dane:
            print(f"ID: {task['id']} | Category:{task['category']}| Tytuł: {task['title']} | Termin: {task['deadline']} | Status: {task['status']} | Priorytet: {task['priority']}")
    except FileNotFoundError:
        print("No file found")


def update_priority(tasks,min_priority,max_priority, K):
    today = datetime.now()
    for task in tasks:
        if 'created_at' not in task or 'user_priority' not in task:
            continue
        created_at = datetime.fromisoformat(task['created_at'])
        days_waiting = (today - created_at).days
        new_priority = min(100, int(task['user_priority'] + K * math.log(days_waiting + 1)))
        task['priority'] = new_priority
def setting_parameters():
    max_days = int(input("What is the maximum number of days after which task should be completed?(e.g.: usually you input tasks in 14 days advance their deadline)\n"))
    max_priority = 100
    min_priority = 1
    K = (max_priority-min_priority)/(math.log(max_days+1))
    params = {
        "min_priority": min_priority,
        "max_priority": max_priority,
        "K": K
    }
    with open('params.json', 'w') as f:
        json.dump(params, f)
    print("Parameters saved.")
    return min_priority, max_priority, K
def saving_history_for_ML(tasks, task_id, new_status):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        print(f"Task with id {task_id} not found.")
        return tasks
    old_status = task.get('status')
    task['status'] = new_status
    if new_status == 'Finished' and old_status != 'Finished':
        task['completed_at'] = datetime.now().isoformat()
    if 'history' not in task:
        task['history'] = []
    change_record = {
        'timestamp': datetime.now().isoformat(),
        'old_status': old_status,
        'new_status': new_status,
        'priority': task.get('priority')
    }
    task['history'].append(change_record)
    return tasks
def export_tasks_to_csv(tasks, filename='tasks_export.csv'):
    headers = ['id', 'category', 'title', 'deadline', 'status', 'priority', 'created_at', 'completed_at', 'time_to_complete_hours']

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        for task in tasks:
            time_to_complete = ''
            if 'completed_at' in task and task['completed_at']:
                created = datetime.fromisoformat(task['created_at'])
                completed = datetime.fromisoformat(task['completed_at'])
                delta = completed - created
                time_to_complete = round(delta.total_seconds() / 3600, 2) 

            row = {
                'id': task.get('id', ''),
                'category': task.get('category', ''),
                'title': task.get('title', ''),
                'deadline': task.get('deadline', ''),
                'status': task.get('status', ''),
                'priority': task.get('priority', ''),
                'created_at': task.get('created_at', ''),
                'completed_at': task.get('completed_at', ''),
                'completion_time':task.get('completion_time',''),
                'time_to_complete_hours': time_to_complete
            }
            writer.writerow(row)

    return filename
def updatetask():
    tasks = load_tasks()
    task_id = int(input("Enter the ID of the task you want to update: "))
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        print("Task not found.")
        return

    new_status = input("Enter new status (Not started, In progress, Finished): ")
    if new_status not in ["Not started", "In progress", "Finished"]:
        print("Invalid status.")
        return

    task['status'] = new_status

    if new_status == "Finished":
        task['completed_at'] = datetime.now().isoformat()
        while True:
            try:
                completion_time = float(input("How many hours did it take to complete this task? \n"))
                task['completion_time'] = completion_time
                break
            except ValueError:
                print("Please enter a valid number for hours.")

    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
    print("Task updated successfully!")