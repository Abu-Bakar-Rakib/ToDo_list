tasks = []
def add_task(title, description):
    task = {
        'title': title,
        'description': description,
        'completed': False
    }
    tasks.append(task)
    print(f"Task '{title}' has been added.")

def view_tasks():
    if not tasks:
        print("No tasks found!")
        return
    for i, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"
        print(f"{i + 1}. {task['title']} - {task['description']} [{status}]")

def mark_task_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        print(f"Task '{tasks[index]['title']}' marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task['title']}' has been deleted.")
    else:
        print("Invalid task number.")
def main_menu():
    while True:
        print("\n--- To-Do List---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_number = int(input("Enter task number to mark as completed: ")) - 1
                mark_task_completed(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                task_number = int(input("Enter task number to delete: ")) - 1
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()