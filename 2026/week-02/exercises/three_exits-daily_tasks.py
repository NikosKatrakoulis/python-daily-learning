# Create three versions of a program that repeatedly asks the user to enter a daily task until they type quit.

# In one version, use a conditional test in the while statement to stop the loop.

# In another version, use an active variable to control how long the loop runs.

# In the third version, use a break statement to exit the loop.

task = ""

while task != 'quit':
    task = input("Enter a daily task(type 'quit' to stop):")

    if task != 'quit':
        print(f"Task added: {task}")


active = True

while active:
    task = input("Enter a daily task(type 'quit' to stop):")

    if task == 'quit':
        active = False
    else:
        print(f"Task added: {task}")

while True:
    task = input("Enter a daily task(type 'quit' to stop):")

    if task == 'quit':
        break

    print(f"Task added: {task}")
