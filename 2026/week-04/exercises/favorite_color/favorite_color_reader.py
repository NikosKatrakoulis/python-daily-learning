# Write a program that asks the user for their favorite color.
# Use json.dumps() to store the color in a file called favorite_color.json.
# Write a separate program that reads the value from the file and prints
# a message like: "I know your favorite color! It's _____."

from pathlib import Path
import json

path = Path("favorite_color.json")
contents = path.read_text()
color = json.loads(contents)

print(f"I know your favorite color! It's {color}.")
