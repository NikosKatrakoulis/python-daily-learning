# A theme park charges different ticket prices depending on height.
# If a person is under 120 cm, the ticket costs $15.
# If the person is between 120 cm and 160 cm, the ticket costs $25.
# If the person is taller than 160 cm, the ticket costs $40.

# Write a loop that asks users for their height and then tells them
# the cost of their ticket.Allow the user to enter quit to stop the program.

prompt = "\nWhat is your height?"
prompt += "\nEnter 'quit' when you are finished."

while True:
    height = input(prompt)
    if height == 'quit':
        break

    height = int(height)

    if height < 120:
        print("Your ticket is $15")
    elif height < 160:
        print("Your ticket is $25")
    else:
        print("Your ticket is $40")
