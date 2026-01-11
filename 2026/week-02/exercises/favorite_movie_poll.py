# Write a program that polls users about their favorite movie.
# Ask for the user’s name and their favorite movie title.
# Store each response in a dictionary.
# Ask if another person would like to respond (yes/no).
# Print all results when finished.

name_prompt = "\nWhat is your name?"
movie_prompt = "What is your favorite movie?"
continue_prompt = "Would you like to let anyone else to respond? (yes/no)"

# THe responses will be stored in the form {name:movie}
responses = {}

while True:
    # Ask the user what is his favorite movie.
    name = input(name_prompt)
    movie = input(movie_prompt)

    # Store the response.
    responses[name] = movie

    # Ask if there's anyone else responding
    repeat = input(continue_prompt)
    if repeat.lower().strip() != 'yes':
        break

# Show the results of the survey.
print("\n--- Results ---")
for name, movie in responses.items():
    print(f"{name.title()}'s favorite movie is {movie.title()}.")
