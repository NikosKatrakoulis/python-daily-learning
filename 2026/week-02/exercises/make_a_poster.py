# Write a function called make_poster() that accepts a size and a slogan.
# The function should print a short summary of the poster size and the slogan
# printed on it.Call the function once using positional arguments and
# once using keyword arguments.

def make_poster(size, slogan):
    """Summarize the poster that is going to be made."""
    print(f"\nI'm going to make a {size} poster.")
    print(f"It will say, '{slogan}'.")


make_poster(
    'XL', 'Tropicana Salsa/Bachata Party Feat. Dimitris Psychogyios & Yolena Kapoli')
make_poster('small', 'Come to visit Mykonos')
