# A gym charges different monthly fees based on age.
# If a person is under 12, the membership is $20 per month.
# If the person is between 12 and 17, the membership is $30 per month.
# If the person is 18 or older, the membership is $50 per month.

# Write a loop that asks users for their age and then tells them the cost of
# their gym membership.Allow the user to enter quit to stop the program.

prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished."

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)

    if age < 12:
        print("Your memberships is $20 per month.")
    elif age < 18:
        print("Your memberships is $30 per month.")
    else:
        print("Your memberships is $50 per month.")
