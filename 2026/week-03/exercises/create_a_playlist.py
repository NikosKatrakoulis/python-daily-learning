# Write a function called create_playlist() that accepts any number of song
# titles.  The function should print a summary of the playlist.
# Call the function three times, each time with a different number of songs.

def create_playlist(*songs):
    """Creat a playlist on spotify with the given songs."""
    print("\nI'll make your playlist on spotify for your trip.")
    for song in songs:
        print(f" ...adding {song} to your playlist.")
    print("Your playlist is ready!")


create_playlist('Hasta Que Tonoci', 'Me Fallaste', 'Mi Musica',
                'Salsakandoo', 'Contra la Coriente')
create_playlist('Hablame', 'Lloraras')
create_playlist('Milestones', 'Blackbird', 'Embraceable you')
