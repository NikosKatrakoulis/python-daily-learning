# Start with your program from Exercise 8-7. Write a while loop that allows
# users to enter an album's artist and title. Once you have that information,
# call make_album() with the user's input and print the dictionary that's
# created. Be sure to include a quit value in the while loop.


def make_album(artist, album, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'Artist': artist.title(),
        'Album': album.title()
    }
    if album_dict:
        album_dict['Tracks'] = tracks
    return


# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of?"
artist_prompt = "Who's the artist"

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:

    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding.")
