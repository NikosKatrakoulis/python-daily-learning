# Expand a program so it remembers more information about a user. Ask the
# user for: their name, their favorite movie, their favorite food.
# Store all this information in a dictionary and save it to a JSON file.
# When the program runs again, read the dictionary from the file and print
# a friendly summary showing everything the program remembers about the user.

from pathlib import Path
import json


def get_stored_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None


def get_new_user_info(path):
    """Get information from a new user."""
    username = input("What's your name?")
    movie = input("What's your favorite movie?")
    food = input("What's your favorite food?")

    user_dict = {
        'name': username,
        'movie': movie,
        'food': food
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict


def greet_user():
    """Greet the user by name and state that we know about them."""
    path = Path("personal_profile_memory.json")
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['name'].title()}!")
        print(f"Hope you've been watching {user_dict['movie'].title()}?")
        print(f"Have you eaten a {user_dict['food']} recently?")
    else:
        user_dict = get_new_user_info(path)
        msg = f"We'll remember you when you will return, {user_dict['name']}."
        print(msg)


greet_user()
