# Write a program that asks the user for their favorite color.
# Use json.dumps() to store the color in a file called favorite_color.json.
# Write a separate program that reads the value from the file and prints
# a message like: "I know your favorite color! It's _____."

from pathlib import Path
import json

color = input("What is your favorite color?")

path = Path("favorite_color.json")
contents = json.dumps(color)
path.write_text(contents)

print("\nThanks! I'll remember the color.")
