# Combine the two programs from favorite_number into one file.
# If the number is already stored, report the favorite number to the user.
# If not, prompt for the user's favorite number and store it in a file.
# Run the program twice to see that it works.

from pathlib import Path
import json

path = Path("favorite_number.json")
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("Waht's your favorite number?")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Thanks, I'll remember that.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")
