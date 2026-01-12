# Start with a function that builds a dictionary describing a movie.
# The function should take in a movie title and the director’s name and
# return a dictionary.Write a while loop that allows users to enter a
# movie title and director. Once the information is entered, call the
# function and print the dictionary that’s created.
# Include a quit value in the loop to stop the program.

def make_movie(director, movie, duration=None):
    """Build a dictionary containing information about a movie."""
    movie_dict = {
        'Director': director.title(),
        'Movie': movie.title(),
    }
    if duration:
        movie_dict['Duration'] = duration
    return movie_dict


# Prepare the prompts.
movie_prompt = "\nWhat movie are you thinking of?"
director_prompt = "Who is the director?"

# Let the user know how to quit.
print("Enter 'quit' to stop.")

while True:

    movie = input(movie_prompt)
    if movie == 'quit':
        break

    director = input(director_prompt)
    if director == 'quit':
        break

    movie = make_movie(director, movie)
    print(movie)

print("\nThanks for responding.")
