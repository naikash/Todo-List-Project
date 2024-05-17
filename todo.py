#Overview:
#A To-Do List application helps users manage their tasks. It allows adding, updating, deleting, and listing tasks. This project will also save the tasks to a file, ensuring persistence between runs.
#Features:
#Add a new task
#Update an existing task
#Delete a task
#List all tasks
#Save tasks to a file
#Load tasks from a file

#Here we Go...

# todo.py
import json

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def to_dict(self):
        return {"description": self.description, "completed": self.completed}

    @staticmethod
    def from_dict(data):
        task = Task(data["description"])
        task.completed = data["completed"]
        return task
#Impelmenting the core functions
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
            return [Task.from_dict(task) for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump([task.to_dict() for task in tasks], file)

def add_task(tasks, description):
    task = Task(description)
    tasks.append(task)

def list_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "Done" if task.completed else "Pending"
        print(f"{i + 1}. {task.description} [{status}]")

def update_task(tasks, index, description):
    if 0 <= index < len(tasks):
        tasks[index].description = description

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index].completed = True
#Building the Command Line Interface     
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Complete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter the task description: ")
            add_task(tasks, description)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            index = int(input("Enter the task number to update: ")) - 1
            description = input("Enter the new description: ")
            update_task(tasks, index, description)
        elif choice == "4":
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == "5":
            index = int(input("Enter the task number to complete: ")) - 1
            complete_task(tasks, index)
        elif choice == "6":
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
