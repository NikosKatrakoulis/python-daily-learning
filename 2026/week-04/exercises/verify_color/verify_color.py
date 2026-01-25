# Write a program that remembers a user’s favorite color. If a favorite color
# is stored in a JSON file, ask the user if this color is still correct.
# If the user confirms, print a message saying you remember their favorite
# color. If the user says it’s not correct, prompt for a new favorite color
# and store it. Run the program twice to test both scenarios.

from pathlib import Path
import json


def get_stored_user_color(path):
    """Get stored user's favorite number if available."""
    if path.exists():
        contents = path.read_text()
        user_color = json.loads(contents)
        return user_color
    else:
        return None


def get_new_user_color(path):
    """Prompt a new user's favorite color."""
    user_color = input("What is your favorite color?")
    contents = json.dumps(user_color)
    path.write_text(contents)
    return user_color


def user_favorite_color():
    """Display the user's favorite color"""
    path = Path("verify_color.json")
    user_color = get_stored_user_color(path)
    if user_color:
        correct = input(f"Is it {user_color} your favorite color? (y/n)")
        if correct == 'y':
            print(
                f"Great to see that I remember that your favorite color is {user_color}.")
            return

    user_color = get_new_user_color(path)
    print(
        f"We'll remember that your favorite color is {user_color} when you will return.")


user_favorite_color()
