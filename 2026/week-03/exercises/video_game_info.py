# Write a function called make_game() that builds a dictionary describing a
# video game. The function should take in a game title and the company that
# developed it, and return a dictionary with this information.
# Create three different game dictionaries and print them.
# Add an optional parameter using None that allows you to store the game’s
# release year. If the release year is provided, include it in the dictionary.
# Make at least one function call that includes the release year.

def make_game(game, company, release_year=None):
    """Build a dictionary containing information about a video game."""
    game_dict = {
        'Game': game.title(),
        'Company': company.title()
    }
    if release_year:
        game_dict['Release Year'] = release_year
    return game_dict


game = make_game("counter stRIKE", "valve", 2023)
print(game)
game = make_game("dota", "valve", 2020)
print(game)
game = make_game(game="call of duty:black ops 7",
                 company="activision", release_year=2025)
print(game)
