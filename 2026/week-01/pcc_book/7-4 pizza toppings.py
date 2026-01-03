# Pizza Toppings: Write a loop that prompts the user to enter a series
# of pizza toppings until they enter a 'quit' value. As they enter each
# topping, print a message saying you’ll add that topping to their pizza.

prompt = "Enter a series of pizza toppings(type 'quit' to finish):"


while True:
    topping = input(prompt)

    if topping == 'quit':
        break

    print(f"I will add {topping} to your pizza.")
