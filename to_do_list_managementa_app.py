# Load existing items
# 1. create a new item
# 2. list items
# 3. mark item as complete
# 4. save items
import json

filename = "todo_list.json"



def load_tasks():
    """loads all previous tasks"""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    """saves current task along same directory as previous tasks"""
    try:
        with open(filename, 'w') as file:
            json.dump(tasks, file)
    except:
        print("Failed to save tasks")

def view_tasks(tasks):
    """display / show tasks to user"""
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("\nThere are not tasks to display")
    else:
        print("Your TO-DO List: ")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")

def create_tasks(tasks):
    """create a new task for user"""
    description = input("\nEnter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task successfully created!")
    else:
        print("Description cannot be empty")
    

def mark_task_complete(tasks):
    """marks task as complete"""
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks):
            tasks["tasks"][task_number - 1]["complete"] = True
            print(f"\nInvalid task number! You have only {task_number} tasks")
            save_tasks(tasks)
        else:
            print("Task marked as complete")
    except:
        print(f"Invalid task number! Enter a valid task number")

def main():
    """diff functions in my program interact here"""
    tasks = load_tasks()


    while True:
        print("\n TO-DO LIST MANAGER")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Complete Tasks")
        print("4. Exit")

        choice = input("Select your choice:\n").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            create_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            print("Goodbye! Thanks for using my TO-DO-LIST App")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4")

main()