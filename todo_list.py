"""
Task 2: To-Do List Application
A command-line to-do list manager that saves tasks to a file (todo_data.json)
so your list is remembered between runs.
"""

import json
import os

DATA_FILE = "todo_data.json"


def load_tasks():
    """Load tasks from the JSON file, or return an empty list if none exist."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Save the current list of tasks to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.\n")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"  [{status}] {i}. {task['title']}")
    print()


def add_task(tasks):
    title = input("Enter the new task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f"Added: {title}\n")
    else:
        print("Task cannot be empty.\n")


def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to mark complete: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked complete.\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']}\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")


def main():
    tasks = load_tasks()
    menu = """
===== TO-DO LIST =====
1. View tasks
2. Add task
3. Mark task as complete
4. Delete task
5. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose 1-5.\n")


if __name__ == "__main__":
    main()
