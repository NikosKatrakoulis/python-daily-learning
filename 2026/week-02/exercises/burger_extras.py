# Write a loop that prompts the user to enter burger extras until they enter
# a quit value. As they enter each extra, print a message saying you’ll add
# that extra to their burger.

prompt = "\nWhat extras would you like on your burger?"
prompt += "\nEnter 'quit' when you are finished:"

while True:
    extras = input(prompt)
    if extras != 'quit':
        print(f"\n\tI will add {extras} to your burger.")
    else:
        break
