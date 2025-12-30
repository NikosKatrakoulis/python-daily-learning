car = 'subaru'
if car == 'subaru':
    print("I predict True.")
    print(f"You have a {car.title()}.")

car = 'audi'
if car != 'subaru':
    print("I predict False.")
    print(f"You have a {car.title()}.")

name = 'niko'
if name == "niko":
    print("I predict True.")
    print(f"Your name is {name.title()}.")

name = 'sofia'
if name != "niko":
    print("I predict False.")
    print(f"Your name is {name.title()}.")

food = 'souvlaki'
if food != 'pizza':
    print("I predict False.")
    print(f"Your favorite food is {food.title()}.")

food = 'souvlaki'
if food == 'souvlaki':
    print("I predict True.")
    print(f"Your favorite food is {food.title()}.")


animal = 'dog'

if animal == 'dog':
    print("\nI predict True.")
if animal == 'cat':
    print("I predict False.")
if animal != 'dog':
    print("I predict False.")
if animal != 'cat':
    print("I predict True.")


city = 'Paris'

if city.lower() == 'paris':
    print("\nI predict True.")
if city.lower() == 'PARIS':
    print("I predict False.")
if city.lower() == 'london':
    print("I predict False.")

score = 75

if score == 75:
    print("\nI predict True")
if score != 75:
    print("I predict False.")
if score > 75:
    print("I predict False.")
if score < 75:
    print("I predict False.")
if score >= 75:
    print("I predict True.")
if score <= 75:
    print("I predict True.")

age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("\nYou can come in.")
if age < 18 or has_ticket:
    print("You can come in.\n")
if age >= 18 and not has_ticket:
    print("This won't be displayed.")

fruits = ['apple', 'banana', 'orange']

if 'apple' in fruits:
    print(True)
if 'kiwi' in fruits:
    print(False)
print("\n")

if 'grape' not in fruits:
    print(True)
if 'banana' not in fruits:
    print(False)
