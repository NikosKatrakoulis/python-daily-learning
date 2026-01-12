# Write a function that builds a dictionary describing a video game.
# The function should take in a game title and the company that developed
# it and return a dictionary. Write a while loop that allows users to enter
# a game title and developer. Call the function with the user’s input and
# print the dictionary that’s created. Include a quit value so users can
# stop entering data.

def make_game(game, company, release_year=None):
    """Build a dictionary containing information about a video game."""
    game_dict = {
        'Game': game.title(),
        'Company': company.title()
    }
    if release_year:
        game_dict['Release Year'] = release_year
    return game_dict


# Prepare the prompts.
game_prompt = "\nWhat video game are you thinking of?"
company_prompt = "Which is the company?"

# Let the user know how to quit.
print("Enter 'quit' to stop.")

while True:

    game = input(game_prompt)
    if game == 'quit':
        break
    company = input(company_prompt)
    if company == 'quit':
        break

    game = make_game(game, company)
    print(game)

print("\nThanks for responding!")
