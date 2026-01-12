# Write a function called make_movie() that builds a dictionary describing a
# movie. The function should take in a director’s name and a movie title,
# and return a dictionary containing these two pieces of information.
# Use the function to create three different movie dictionaries and print
# each one. Add an optional parameter using None that allows you to store
# the movie’s duration (in minutes). If a value is provided, include it
# in the dictionary. Make at least one function call that includes the
# duration.

def make_movie(director, movie, duration=None):
    """Build a dictionary containing information about a movie."""
    movie_dict = {
        'Director': director.title(),
        'Movie': movie.title(),
    }
    if duration:
        movie_dict['Duration'] = duration
    return movie_dict


movie = make_movie("Francis Coppola", "Godfather", 175)
print(movie)
movie = make_movie("christopher NOlan", "dark knight", 152)
print(movie)
movie = make_movie("steven Spielberg", "schindler's list", 195)
print(movie)
