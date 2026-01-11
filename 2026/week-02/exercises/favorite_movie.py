# Write a function called favorite_movie() that accepts one parameter, title.
# The function should print a message like: One of my favorite movies
# is Inception.Call the function with a movie title as an argument.

def favorite_movie(title):
    """Display a message about someone's favorite movie."""
    print(f"One of my favorite movies is {title.title()}.")


favorite_movie('godfather')
