# Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing
# different albums. Print each return value to show that the dictionaries are
# storing the album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value
# for the number of songs, add that value to the album’s dictionary. Make at
# least one new function call that includes the number of songs on an album.


def make_album(artist, title):
    album_dict = {
        'Artist': artist.title(),
        'Album': title.title(),
    }
    return album_dict


album = make_album('miles davis', 'kind of blue')
print(album)

album = make_album('john coltrane', 'blue train')
print(album)

album = make_album('wes montgomery', 'full house')
print(album)


def make_album(artist, title, tracks=None):
    album_dict = {
        'Artist': artist.title(),
        'Album': title.title(),
    }
    if tracks:
        album_dict['Tracks'] = tracks
    return album_dict


album = make_album('miles davis', 'kind of blue')
print(album)

album = make_album('john coltrane', 'blue train')
print(album)

album = make_album('wes montgomery', 'full house', tracks=5)
print(album)
