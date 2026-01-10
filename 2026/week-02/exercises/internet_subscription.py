# An internet provider offers different plans based on age.
# If a person is under 18, the plan costs $15 per month.
# If the person is between 18 and 64, the plan costs $30 per month.
# If the person is 65 or older, the plan costs $20 per month.

# Write a loop that asks users for their age and then tells them the cost
# of their internet subscription.Allow the user to enter quit to stop the
# program.

prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished."

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)

    if age < 18:
        print("You plan costs $15 per month.")
    elif age < 64:
        print("You plan costs $30 per month.")
    else:
        print("You plan costs $20 per month.")
