import task_manager as t
def main():
    choice = input("What action do you want to take? \n Add task \n Update task \n View tasks ")

    match choice:
        case "Add task":
            t.addtask()

        case "Update task":
            t.updatetask()

        case "View tasks":
            t.viewtasks()
        case _:
            print("No option found")



if __name__ == "__main__":
    main()