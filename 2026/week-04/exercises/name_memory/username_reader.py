# Write a program that prompts the user for their name.
# Store the name in a JSON file called username.json.

# Write another program that reads the stored name and prints a
# greeting such as:

# "Welcome back, _____! I remember you."

from pathlib import Path
import json

path = Path("username.json")
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}! I remember you.")
