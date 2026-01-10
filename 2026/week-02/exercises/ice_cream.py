# Write a loop that asks the user to enter ice cream flavors until they
# type quit. For each flavor, print a message saying you’ll add that flavor
# to the ice cream.

prompt = "\nWhat ice cream flavors would you like on your cake?"
prompt += "\nEnter 'quit' when you are finished:"

while True:
    flavor = input(prompt)
    if flavor != 'quit':
        print(f"\n\tI will add {flavor} to your cake.")
    else:
        break
