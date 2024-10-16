import json
import os  

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

def load_tasks():
    if os.path.exists('tasks.json') and os.path.getsize('tasks.json') > 0:
        with open('tasks.json', 'r') as f:
            try:
                return [Task(**data) for data in json.load(f)]
            except json.JSONDecodeError:
                print("Error: The tasks.json file is corrupted. Starting with an empty task list.")
                return []
    else:
        return []

def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (Work, Personal, Urgent): ")
            tasks.append(Task(title, description, category))
            print("Task added successfully.")
            
        elif choice == '2':
            if tasks:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task.completed else "✗"
                    print(f"{i}. [{status}] {task.title} - {task.description} [{task.category}]")
            else:
                print("No tasks available.")
                
        elif choice == '3':
            if not tasks:
                print("No tasks available to mark as completed.")
            else:
                try:
                    task_num = int(input("Enter task number to mark as completed: ")) - 1
                    if 0 <= task_num < len(tasks):
                        tasks[task_num].mark_completed()
                        print("Task marked as completed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
                
        elif choice == '4':
            if not tasks:
                print("No tasks available to delete.")
            else:
                try:
                    task_num = int(input("Enter task number to delete: ")) - 1
                    if 0 <= task_num < len(tasks):
                        tasks.pop(task_num)
                        save_tasks(tasks)
                        print("Task deleted successfully.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
                
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
            
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
