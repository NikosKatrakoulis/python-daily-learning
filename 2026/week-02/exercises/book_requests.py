# Write different versions of either Exercise 7-4 or 7-5 that do each of
# the following at least once: Use a conditional test in the while
# statement to stop the loop. Use an active variable to control how
# long the loop runs. Use a break statement to exit the loop when the
# user enters a 'quit' value.

prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished."

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("You get in free!")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
