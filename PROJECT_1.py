import sys

print("✨ 👋 Welcome to your Personal To-Do List Manager! ✨")
print("Glad to have you here. How can I help you organize your day today?")
# 1. Menu Function
def show_menu():
    print("\n📌 Please select an action:")
    print("  [1] ➕ Add New Task")
    print("  [2] 👁️  View All Tasks")
    print("  [3] 🗑️  Delete Task")
    print("  [4] 🚪 Exit")
    return input("\n👉 Enter your choice (1-4): ").strip()
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
# 4. delet tasks
def delete_task(tasks):
    if not tasks:
        print("\n  No tasks available to delete.")
        return
        
    view_tasks(tasks)
    try:
        task_num = int(input("\n👉 Enter task list number to delete: ").strip())
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"\n🗑️  Task '{removed['title']}' deleted successfully!")
        else:
            print("\n⚠️ Invalid task number! Please select from the list.")
    except ValueError:
        print("\n⚠️ Please enter a valid number.")
# 5. Main Loop
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

        elif choice=="3":
            delete_task(tasks)

        elif choice == "4":
            print("\nProgram finished. Goodbye!")
            break  # Stops the loop and exits naturally

        else:
            print("[!] Invalid option! Please enter 1, 2, or 3.")

# 5. Program Entry Point (Outside main)
if __name__ == "__main__":
    main()