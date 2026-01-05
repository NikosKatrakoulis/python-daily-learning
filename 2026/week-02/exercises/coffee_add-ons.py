# Write a loop that prompts the user to enter coffee add-ons
# (e.g., sugar, milk, cinnamon) until they type quit. After each add-on,
# print a message saying you’ll add that add-on to their coffee.


while True:
    addoon = input("Enter coffee add-ons(type 'quit' to stop):")

    if addoon == 'quit':
        break

    print(f"I will add {addoon} to your coffee.")
