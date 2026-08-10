import sys

# 1. Menu Function
def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    return input("Enter your choice (1-3): ").strip()

# 2. Add Task Function
def add_task(tasks, tasktitle):
    task_id = len(tasks) + 1
    new_task = {"id": task_id, "title": tasktitle}
    tasks.append(new_task)
    print(f"Task '{tasktitle}' added with ID {task_id}.")

# 3. View Task Function (Fixed name to match main)
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\n--- YOUR TASKS ---")
        for index, item in enumerate(tasks, start=1):
            print(f"{index}. [ID: {item['id']}] {item['title']}")

# 4. Main Loop
def main():
    tasks = []

    while True:
        choice = show_menu()

        if choice == "1":
            title = input("Enter task name: ").strip()
            if title:
                add_task(tasks, title)
            else:
                print(" Task cannot be empty.")
        
        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            print("\nProgram finished. Goodbye!")
            break  # Stops the loop and exits naturally

        else:
            print("[!] Invalid option! Please enter 1, 2, or 3.")

# 5. Program Entry Point (Outside main)
if __name__ == "__main__":
    main()