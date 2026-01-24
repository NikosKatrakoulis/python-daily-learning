# Write one program that remembers the user’s name. If a file containing
# the user’s name exists, greet the user by name. If the file does not exist,
# ask the user for their name and store it using JSON. Run the program twice
# to confirm that the name is remembered.

from pathlib import Path
import json


path = Path("username.json")

try:
    contents = path.read_text()
except FileNotFoundError:
    username = input("What is your username?")
    contents = json.dumps(username)
    path.write_text(contents)
    print("Thanks! I'll remember that.")
else:
    contents = path.read_text()
    username = json.loads(contents)
    print(f"I know your username on GitHub! It's {username}.")
