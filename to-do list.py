tasks = {}

def add_task(task_name):
    if task_name not in tasks:
        tasks[task_name] = False
        print(f"Task '{task_name}' added.")
    else:
        print("Task already exists.")

def complete_task(task_name):
    if task_name in tasks:
        tasks[task_name] = True
        print(f"Task '{task_name}' completed.")
    else:
        print("Task not found.")

def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task, completed in tasks.items():
            status = "Completed" if completed else "Incomplete"
            print(f"{task}: {status}")

def main():
    while True:
        print("\n1. Add Task")
        print("2. Complete Task")
        print("3. Show Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == "2":
            task_name = input("Enter task name to complete: ")
            complete_task(task_name)
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
