# Write a single program that checks if a user’s favorite color is
# already stored in a JSON file. If the file exists, print a message
# saying you remember the user’s favorite color. If the file does not
# exist, prompt the user to enter their favorite color and store it
# in the file. Run the program twice to verify that it remembers the
# color on the second run.

from pathlib import Path
import json

path = Path("favorite_color.json")
try:
    contents = path.read_text()
except FileNotFoundError:
    color = input("What is your favorite color?")
    contents = json.dumps(color)
    path.write_text(contents)
    print("Thanks, I'll remember that!")
else:
    contents = path.read_text()
    color = json.loads(contents)
    print(f"I know your favorite color! It's {color}.")
