
tasks = []

def display_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n--- Student Tasks ---")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} - {status}')


def add_task():
    title = input("Enter task title: ")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def complete_task():
    if not tasks:
        print("No tasks available to complete.")
        return

    display_tasks()

    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("Task is already completed.")
            else:
                task["completed"] = True
                print("Task marked as completed!")
            return

    print("Task ID not found.")



def main():
    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")
        print("4. Complete Task")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        elif choice == "4":
            complete_task()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
