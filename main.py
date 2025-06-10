import task_manager as t
def main():
    choice = input("What action do you want to take? \n 1. Add task \n 2. Update task \n 3. View tasks \n 4. Set parameters \n")

    match choice:
        case 'Add task':
            t.addtask()

        case 'Update task':
            t.updatetask()

        case 'View tasks':
            t.viewtasks()
        case 'Set parameters':
            t.setting_parameters()
        case _:
            print("No option found")



if __name__ == "__main__":
    main()