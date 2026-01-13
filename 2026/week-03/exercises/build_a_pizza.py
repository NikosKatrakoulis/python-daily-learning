# Write a function called make_pizza() that accepts any number of toppings.
# The function should print a summary of the pizza that is being made.
# Call the function three times, each time using a different number of
# toppings.

def make_pizza(*toppings):
    """Make a pizza with the given toppings."""
    print("\nI'll make you a great pizza.")
    for topping in toppings:
        print(f" ...adding {topping} to your pizza.")
    print("Your pizza is ready!")


make_pizza('tomato sauce', 'motzarella', 'basilico')
make_pizza('tomato sauce', 'motzarella', 'green peppers', 'mushrooms')
make_pizza('mushrooms', 'motzarella', 'cream of katsikisio cheese')
