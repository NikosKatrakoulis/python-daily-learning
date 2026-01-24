# Write a program that prompts the user for their name.
# Store the name in a JSON file called username.json.

# Write another program that reads the stored name and prints a
# greeting such as:

# "Welcome back, _____! I remember you."

from pathlib import Path
import json

username = input("What is your username?")

path = Path("username.json")
contents = json.dumps(username)
path.write_text(contents)

print("Thanks! I'll remember your username.")
