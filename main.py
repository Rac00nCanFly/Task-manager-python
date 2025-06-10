import task_manager as t
def main():
    choice = input("What action do you want to take? \n 1. Add task \n 2. Update task \n 3. View tasks \n 4. Set parameters \n Input number between 1-4")

    match choice:
        case 1:
            t.addtask()

        case 2:
            t.updatetask()

        case 3:
            t.viewtasks()
        case 4:
            t.setting_parameters()
        case _:
            print("No option found")



if __name__ == "__main__":
    main()