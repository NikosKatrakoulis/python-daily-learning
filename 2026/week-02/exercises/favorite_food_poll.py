# Write a program that polls users about their favorite food.
# Ask for the user’s name and their favorite food.
# Store the responses in a dictionary.
# Ask if another person wants to respond (yes/no).
# After the poll ends, print the results.

name_prompt = "\nWhat is your name?"
food_prompt = "What is your favorite food?"
continue_prompt = "Would you like to let someone else to respond? (yes/no)"

# The responses will be stored in the form {name:food}
responses = {}

while True:
    # Ask the user what is his favorite food.
    name = input(name_prompt)
    food = input(food_prompt)

    # Store the response.
    responses[name] = food

    # Ask if there is anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show the results of the survey.
print("\n--- Results ---")
for name, food in responses.items():
    print(f"{name.title()} 's favorite food is {food}.")
