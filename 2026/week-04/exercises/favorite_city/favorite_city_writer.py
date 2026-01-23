# Write a program that asks the user for their favorite city.
# Save the city to a file called favorite_city.json using JSON.

# Write a second program that reads the file and prints a message like:

# "I remember! Your favorite city is _____."

from pathlib import Path
import json

city = input("What is your favorite city?")

path = Path("favorite_city.json")
contents = json.dumps(city)
path.write_text(contents)

print("Thanks! I'll remember your favorite city.")
