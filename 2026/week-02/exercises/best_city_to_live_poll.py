# Write a program that polls users about the best city to live in.
# Ask for the user’s name and which city they think is the best to live in.
# Save the answers in a dictionary.
# Continue polling until the user says no.
# Print the results at the end.

name_prompt = "\nWhat is your name?"
best_city_to_live_prompt = "What is the best city to live?"
continue_prompt = "\nWould you like to ask anyone else to respond? (yes/no)"

# Responses will be stored in form{name:best city to live}
responses = {}

while True:
    # Ask the user what is his best city to live.
    name = input(name_prompt)
    best_city = input(best_city_to_live_prompt)

    # Store the responses
    responses[name] = best_city

    # Ask if there's anyone else responding
    repeat = input(continue_prompt)
    if repeat.lower().strip() != 'yes':
        break

# Show the results of the survey.
print("\n--- Results ---")
for name, best_city in responses.items():
    print(f"{name.title()}'s best city is {best_city.title()}.")
