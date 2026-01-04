# Three Exits: Write different versions of either Exercise 7-4 or 7-5
# that do each of the following at least once: Use a conditional test in
# the while statement to stop the loop. Use an active variable to control
# how long the loop runs. Use a break statement to exit the loop when the
# user enters a 'quit'.

topping = ""

while topping != 'quit':
    topping = input("Enter a pizza topping (type 'quit' to stop):")

    if topping != 'quit':
        print(f"i will add {topping} to your pizza")


active = True

while active:
    topping = input("Enter a series of pizza toppings(type 'quit' to finish):")

    if topping == 'quit':
        active = False

    print(f"i will add {topping} to your pizza.")


while True:
    topping = input("Enter a series of pizza toppings(type 'quit' to finish):")

    if topping == 'quit':
        break
    print(f"I will add {topping} to your pizza.")
