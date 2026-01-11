# Saving data with json is useful when you’re working with
# user-generated data, because if you don’t store your user’s
# information somehow, you’ll lose it when the program stops
# running. Let’s look at an example where we prompt the user
# for their name the first time they run a program and then
# remember their name when they run the program again.
# Let’s start by storing the user’s name:

# from pathlib import Path
# import json

# username = input("What is your name? ")

# path = Path(
#     "C://Dev//python-daily-learning//2026//week-02//pcc_book//username.json")
# contents = json.dumps(username)

# path.write_text(contents)

# print(f"We'll remember you when you come back, {username}!")


# We could write a try-except block here to respond
# appropriately if username.json doesn’t exist, but instead
# we’ll use a handy method from the pathlib module:

# from pathlib import Path
# import json

# path = Path(
#     "C://Dev//python-daily-learning//2026//week-02//pcc_book//username.json")
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}!")
# else:
#     username = input("What is your name? ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}!")


# from pathlib import Path
# import json


# def greet_user():
#     """Greet the user by name."""
#     path = Path(
#         "C://Dev//python-daily-learning//2026//week-02//pcc_book//username.json")
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")


# greet_user()


# Let’s refactor greet_user() so it’s not doing so many
# different tasks. We’ll start by moving the code for retrieving
# a stored username to a separate function:

# from pathlib import Path
# import json


# def get_stored_username(path):
#     """Get stored username if available."""
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username
#     else:
#         None


# def greet_user():
#     path = Path(
#         "C://Dev//python-daily-learning//2026//week-02//pcc_book//username.json")
#     username = get_stored_username
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")


# greet_user()

# We should factor one more block of code out of
# greet_user(). If the username doesn’t exist, we should move
# the code that prompts for a new username to a function
# dedicated to that purpose:

from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path(
        "C://Dev//python-daily-learning//2026//week-02//pcc_book//username.json")
    contents = path.read_text()
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
