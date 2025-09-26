import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "done": status == "done"})
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for t in tasks:
            status = "done" if t["done"] else "pending"
            file.write(f"{t['task']}|{status}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.\n")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "⏳"
        print(f"{i}. {t['task']} [{status}]")
    print()

def add_task(tasks):
    new_task = input("Enter a new task: ").strip()
    if new_task:
        tasks.append({"task": new_task, "done": False})
        print("Task added!\n")
    else:
        print("Empty task not added.\n")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("Mark which task as done (number)? "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            print("Marked as done!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        choice = int(input("Delete which task (number)? "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Deleted: {removed['task']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("---- TO-DO LIST MENU ----")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
