# Write a loop that prompts the user to enter sandwich toppings until they
# enter quit.As each topping is entered, print a message confirming it was
# added to the sandwich.

prompt = "\nWhat toppings would you like on your sandwich?"
prompt += "\nEnter 'quit' when you are finished:"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"\n\tI will add {topping} to your sandwich.")
    else:
        break
