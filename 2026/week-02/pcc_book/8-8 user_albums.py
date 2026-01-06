# User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have
# that information, call make_album() with the user’s input and print the
# dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album(artist, title, tracks=0):
    album_dict = {
        'Artist': artist,
        'Album': title
    }

    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


title_prompt = "\nWhat album are you thinking of?"
artist_prompt = "Who's the artist?"

print("Enter 'quit' at any time to stop.")


while True:
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    title = input(title_prompt)
    if title == 'quit':
        break

    album = make_album(artist.title(), title.title())
    print(f"\nAlbum Info:\n{album}")
