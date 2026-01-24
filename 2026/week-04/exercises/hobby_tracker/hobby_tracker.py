# Write a program that remembers a user’s hobbies.
# Ask the user for: their name, their main hobby and how many hours per week
# they spend on it. Store the information in a dictionary and save it to
# a JSON file. When the program runs again, load the dictionary and print
# a message summarizing the user’s hobby habits.

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
    name = input("What's your name?")
    hobby = input("What's your favorite hobby?")
    hours = input("How many hours per week do you spend on it?")

    user_dict = {
        'name': name,
        'hobby': hobby,
        'hours': hours
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict


def greet_user():
    """Greet the user by name and state that we know about them."""
    path = Path("hobby_tracker.json")
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['name'].title()}!")
        print(f"Hope you've  practiced {user_dict['hobby']} this week.")
        print(f"You practiced {user_dict['hours']} this week, right?")
    else:
        user_dict = get_new_user_info(path)
        msg = f"We'll remember you when you'll return {user_dict['name'].title()}."
        print(msg)


greet_user()
