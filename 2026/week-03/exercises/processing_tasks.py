# Make a list called tasks filled with several tasks
# (e.g., "email client", "write report").
# Write a function called show_tasks() that prints all tasks.
# Write a function called complete_tasks() that prints each task as
# it is completed and moves it to a list called completed_tasks.
# After running the program, print both lists to verify the tasks
# were moved correctly.


def show_tasks(tasks):
    """Print all tasks in the list."""
    for task in tasks:
        print(task)


def complete_tasks(tasks, completed_tasks):
    "Printing each task and then move it to completed_tasks."
    print("\nSending all tasks:")
    while tasks:
        current_task = tasks.pop()
        print(current_task)
        completed_tasks.append(current_task)


tasks = ["email client", "write report", "meeting with the team"]
show_tasks(tasks)

completed_tasks = []
complete_tasks(tasks, completed_tasks)

print("\nFinal lists:")
print(tasks)
print(completed_tasks)
