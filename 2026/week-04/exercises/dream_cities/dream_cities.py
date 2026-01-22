# Write a program that repeatedly asks users to enter the name of a city
# they want to visit. Save all city names to a file called dream_cities.txt,
# with each city on a new line. Allow the user to exit by typing 'quit'.

from pathlib import Path

path = Path("dream_cities.txt")


prompt = "\nWhat is the name of the city you would like to visit?"
prompt += "\nEnter 'quit' to quit if you are the last."

dream_cities = []

while True:
    city = input(prompt)
    if city == 'quit':
        break

    print("\nThank you for the response.")
    dream_cities.append(city)

city_string = ''
for city in dream_cities:
    city_string += f"{city}\n"

path.write_text(city_string)
