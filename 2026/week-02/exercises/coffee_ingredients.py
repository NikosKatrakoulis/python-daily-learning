# Write a loop that asks the user to enter coffee ingredients until they
# type quit.For each ingredient entered, print a message saying you’ll add
# it to the coffee.

prompt = "\nWhat ingredients would you like on your coffee?"
prompt += "\nEnter 'quit' when you are finished:"

while True:
    ingredient = input(prompt)
    if ingredient != 'quit':
        print(f"\n\tI will add {ingredient} to your coffee.")
    else:
        break
