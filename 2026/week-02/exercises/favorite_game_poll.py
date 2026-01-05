# Write a program that polls users about their favorite video game.
# Use a prompt like: "What is your favorite video game?" Ask for
# the user’s name too. Store responses in a dictionary. When the
# poll ends, print the results (each person’s name and their chosen game).

responses = {}

while True:
    name = input("What is your name?")
    response = input("What is your favorite video game?")

    responses[name] = response

    repeat = input("Would you let another one to respond?(yes/no)")
    if repeat == 'no':
        break

print("---Poll Results---")
for name, game in responses.items():
    print(f"{name.title()}'s favorite game is {game.title()}")
