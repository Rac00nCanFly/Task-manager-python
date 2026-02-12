# Task Manager (CLI)

A simple command-line **task management application** written in Python.  
It lets you add, view, and update tasks, automatically adjusts their priority over time, and exports history for further data analysis or machine learning.

## Features

- Add tasks with:
  - title
  - category
  - deadline (`dd-mm-yyyy`)
  - status (`Not started`, `In progress`, `Finished`)
  - priority (1–100)

- View tasks sorted by:
  - **dynamic priority** (user priority updated over time)
  - deadline

- Configure priority growth:
  - parameter `K` computed from expected maximum days to complete a task
  - priority grows with time based on a logarithmic function

- Update tasks:
  - change status
  - store completion time (hours)
  - record completion timestamp

- Export to CSV:
  - task metadata
  - creation and completion timestamps
  - computed `time_to_complete_hours`
  - ready for further analysis / ML experiments

## Tech Stack

- **Language**: Python 3
- **Libraries**: `json`, `csv`, `datetime`, `math`, `os`
- **Data storage**: local JSON files (`tasks.json`, `params.json`)
- **Output**: CSV export for analysis

## How to Run

```bash
git clone https://github.com/Rac00nCanFly/Task-manager-python.git
cd Task-manager-python
python main.py
```
Follow the menu to:
- add a task
- update an existing task
- view all tasks
- set priority parameters

How Priority Works
```
    User defines:

        maximum number of days after which tasks should be completed

    The app computes a constant K so that:

        priority grows from min_priority to max_priority over that period

    For each task:

        age in days is computed from created_at

        new priority = user_priority + K * log(days_waiting + 1) (capped at 100)

This makes older tasks gradually bubble up in the list, even if their original priority was low.
```
Possible Improvements
- Add basic unit tests
- Add a simple GUI or web interface
- Use a real database instead of JSON (e.g. SQLite)
- More advanced analytics / ML on exported task history
