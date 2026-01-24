# Write a program that stores and remembers the user’s favorite city.
# If the city is already stored in a JSON file, print a message confirming
# that you remember it. If the file does not exist, ask the user to enter
# their favorite city and save it. Run the program twice to make sure it
# works correctly.

from pathlib import Path
import json

path = Path("favorite_city.json")

try:
    contents = path.read_text()
except FileNotFoundError:
    city = input("What is your favorite city?")
    contents = json.dumps(city)
    path.write_text(contents)
    print("Thanks, I'll remember that.")
else:
    contents = path.read_text()
    city = json.loads(contents)
    print(f"I know your favority city! It's {city.title()}.")
