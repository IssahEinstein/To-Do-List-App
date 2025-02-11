# To-Do List Management App

## Description
The To-Do List Management App is a simple command-line application that allows users to efficiently manage their tasks. Users can create tasks, view their to-do list, mark tasks as complete, and save their progress for future use. The application uses a JSON file (`todo_list.json`) to store tasks persistently.

## Features
- Add new tasks with a description
- View all existing tasks
- Mark tasks as complete
- Save and load tasks automatically

## Files
- `to_do_list_managementa_app.py`: The main Python script that runs the application.
- `todo_list.json`: A JSON file used to store the tasks persistently.

## Requirements
- Python 3.x

## How to Use
1. Run the script:
   ```bash
   python to_do_list_managementa_app.py
   ```
2. Choose an option from the menu:
   - `1`: View Tasks
   - `2`: Add a New Task
   - `3`: Mark a Task as Complete
   - `4`: Exit

## Functionality
- `load_tasks()`: Loads previously saved tasks from `todo_list.json`.
- `save_tasks(tasks)`: Saves the current list of tasks to `todo_list.json`.
- `view_tasks(tasks)`: Displays all tasks along with their completion status.
- `create_tasks(tasks)`: Prompts the user to enter a new task and saves it.
- `mark_task_complete(tasks)`: Allows the user to mark a task as complete.
- `main()`: Runs the main loop to interact with the user.

## Known Issues
- The error handling for marking tasks as complete needs improvement.
- The script does not validate duplicate tasks.

## Future Enhancements
- Implement a graphical user interface (GUI).
- Add a feature to delete tasks.
- Allow task prioritization.
- Implement a due date feature for tasks.

## Author
- Developed byIssah Abdullah (iabdullah@stetson.edu)

## License
This project is open-source and available for modification and distribution under the MIT License.

