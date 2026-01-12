# Write a function called artist_album() that takes in an artist name and an
# album title. The function should return a string formatted like this:
# "Nirvana – Nevermind".Call the function with at least three artist–album
# pairs, and print the returned values.

def artist_album(artist_name, album_title):
    """Return a string."""
    return f"\n{artist_name.title()} - {album_title.title()}"


album = artist_album("miles davis", "milestones")
print(album)
album = artist_album("john coltrane", "blue train")
print(album)
album = artist_album("art blakey", "moanin'")
print(album)
