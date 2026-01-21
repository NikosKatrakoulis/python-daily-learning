# Write a program that repeatedly asks users to enter their favorite food.
# Collect all the foods entered and write them to a file called favorite_foods.txt.
# Make sure each food is written on a new line.
# Allow users to quit by entering 'quit'.

from pathlib import Path

path = Path("favorite_foods.txt")

prompt = "\nWhat is your favorite food?"
prompt += "\nEnter 'quit' when if you are the last."

favorite_foods = []
while True:
    food = input(prompt)
    if food == 'quit':
        break

    print(f"Thanks for adding your favorite book in the list.")
    favorite_foods.append(food)

food_string = ''
for food in favorite_foods:
    food_string += f"{food}\n"

path.write_text(food_string)
