# Create a file called task_functions.py that contains functions related to
# managing tasks. One function should process pending tasks and move them
# to a completed list. Another function should display all completed tasks.
# Create a second file called task_manager.py.
# In this file, import the functions from task_functions.py and use
# them to process a list of tasks.

def show_tasks(tasks):
    for task in tasks:
        print(task)


def completed_tasks(tasks, completed_tasks):
    while tasks:
        current_task = tasks.pop()
        print(current_task)
        completed_tasks.append(completed_tasks)
