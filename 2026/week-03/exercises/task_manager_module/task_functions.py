# Create a file called task_functions.py that contains functions related to
# managing tasks. One function should process pending tasks and move them
# to a completed list. Another function should display all completed tasks.
# Create a second file called task_manager.py.
# In this file, import the functions from task_functions.py and use
# them to process a list of tasks.

"""Functions related to managing tasks."""


def show_tasks(tasks, completed_tasks):
    while tasks:
        current_task = tasks.pop()
        print(f"Task: {current_task}")
        completed_tasks.append(current_task)


def show_completed_tasks(completed_tasks):
    print("\nThe following tasks have been done:")
    for completed_task in completed_tasks:
        print(completed_task)
