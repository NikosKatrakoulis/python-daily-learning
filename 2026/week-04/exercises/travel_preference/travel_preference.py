# Write a program that remembers a user’s travel preferences.
# Ask the user for: their name, their favorite country and their dream travel
# destination. Store the information in a dictionary and write it to a
# JSON file. When the program is run again, read the data and print a
# summary explaining what the program remembers about the user’s travel
# preferences.

from pathlib import Path
import json


def get_stored_user_info(path):
    """Get stored user information if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None


def get_new_user_info(path):
    """Get information from a new user."""
    name = input("What's your name?")
    coutry = input("What's your favorite country?")
    dream_destination = input("What's your dream travel destination?")

    user_dict = {
        'name': name.title(),
        'country': coutry.title(),
        'destination': dream_destination.title()
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict


def greet_user():
    """Greet the user by name and state that we know about them."""
    path = Path("travel_preference.json")
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['name']}!")
        print(f"Is it still {user_dict['country']} your favorite country?")
        print(
            f"Did you manage to visit your dream destination {user_dict['destination']}?")
    else:
        user_dict = get_new_user_info(path)
        msg = f"We'll remember you when you'll return,{user_dict['name']}!"
        print(msg)


greet_user()
