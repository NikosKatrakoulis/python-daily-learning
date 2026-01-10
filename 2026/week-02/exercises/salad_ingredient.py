# Write a loop that prompts the user to enter salad ingredients until
# they enter quit. As each ingredient is entered, print a message
# confirming it was added to the salad.

prompt = "\nWhat ingredients would you like on your salad bowl?"
prompt += "\nEnter 'quit' when you are finished:"

while True:
    ingredient = input(prompt)
    if ingredient != 'quit':
        print(f"\nI will add {ingredient} to your salad bown.")
    else:
        break
