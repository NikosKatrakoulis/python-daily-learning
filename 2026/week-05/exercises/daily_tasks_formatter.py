# Ask the user to enter their daily tasks in one line, separated by commas
# (for example: "study, workout, cook dinner").
# Use split(',') to create a list of tasks
# Clean up extra spaces around each task
# Print the tasks joined by " -> " using join()

daily_tasks = input("Enter your daily tasks in one line, separeted by commas:")

tasks = daily_tasks.split(",")

clean_tasks = []

for task in tasks:
    clean_tasks.append(task.strip())

result = " | ".join(clean_tasks)
print(result)
