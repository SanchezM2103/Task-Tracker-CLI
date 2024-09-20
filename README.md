# Task-Tracker-CLI
(https://roadmap.sh/projects/task-tracker)

Repository to do a Task Tracker using CLI (Command Line Interface)

The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress
Here are some constraints to guide the implementation:

You can use any programming language to build this project.
Use positional arguments in command line to accept user inputs.
Use a JSON file to store the tasks in the current directory.
The JSON file should be created if it does not exist.
Use the native file system module of your programming language to interact with the JSON file.
Do not use any external libraries or frameworks to build this project.
Ensure to handle errors and edge cases gracefully.

- python taskapp.py add "..."

- python taskapp delete (element n)

- python taskapp delete (deletes everything)

- python taskapp deletefile

- python taskapp mark -p (In progress) or -d (Done)

- python taskapp.py list

- python taskapp.py listdone

- python taskapp.py listnotdone

- python taskapp.py currentlist
