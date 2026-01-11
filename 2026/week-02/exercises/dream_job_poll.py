# Write a program that polls users about their dream job.
# Ask for the user’s name and what job they would love to have.
# Store the answers in a dictionary.
# Keep asking new users until someone enters no.
# Print the results at the end.

name_prompt = "\nWhat is your name?"
dream_job_prompt = "If you would like to do a job, what would it be?"
continue_prompt = "\nWould you like to let someone else respond? (yes/no)"

# Responses will be stored in form {name:dream job}
responses = {}

while True:
    # Ask the user what is his dream job.
    name = input(name_prompt)
    dream_job = input(dream_job_prompt)

    # Store the responses.
    responses[name] = dream_job

    # Ask if there's anyone else responding
    repeat = input(continue_prompt)
    if repeat.lower().strip() != 'yes':
        break

# Show the results of the survey.
print("\n--- Results ---")
for name, dream_job in responses.items():
    print(f"{name.title()} 's dream job is {dream_job}.")
