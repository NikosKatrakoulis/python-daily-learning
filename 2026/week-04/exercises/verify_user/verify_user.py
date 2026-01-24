# The final listing for remember_me.py assumes either that the user has
# already entered their username or that the program is running for the
# first time. We should modify it in case the current user is not the
# person who last used the program. Before printing a welcome back
# message in greet_user(), ask the user if this is the correct username.
# If it's not, call get_new_username() to get the correct username.

from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt a new username."""
    username = input("What is your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path("verify_user.json")
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (y/n)")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            return

    # We got a username, but it's not correct.
    # Prompt for a new username.
    username = get_new_username(path)
    print(f"We'll remember you when you come back, {username}!")


greet_user()
