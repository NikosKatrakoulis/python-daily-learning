# Write a loop that prompts the user to enter ice cream toppings until they
# enter quit.For each topping entered, print a message saying you’ll add
# that topping to their ice cream.

while True:
    toppings = input("Enter ice cream toppings(type 'quit' to stop):")

    if toppings == 'quit':
        break

    print(f"I will add {toppings} to your ice cream.")
