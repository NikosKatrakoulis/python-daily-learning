# Write a function called favorite_game() that accepts one parameter, name.
# The function should print a message like: My favorite game is Minecraft.
# Call the function with a game name as an argument.

def favorite_game(name):
    """Display a message about someone's favorite game."""
    print(f"My favorite game is {name.title()}.")


favorite_game('cs go')
