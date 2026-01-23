# Write a program that asks the user for their favorite city.
# Save the city to a file called favorite_city.json using JSON.

# Write a second program that reads the file and prints a message like:

# "I remember! Your favorite city is _____."

from pathlib import Path
import json

path = Path("favorite_city.json")
contents = path.read_text()
city = json.loads(contents)

print(f"I remember! Your favorite city is {city.title()}.")
