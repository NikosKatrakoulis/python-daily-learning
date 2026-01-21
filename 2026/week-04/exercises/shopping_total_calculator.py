# Write a program that repeatedly asks the user for the prices of two items
# and prints their total cost. Use a while loop to keep the program running.
# Allow quitting with 'q'. Handle invalid input with try-except.
# Print a friendly message if the input is not a valid number.

print("Enter 'q' at any time to quit.")

while True:
    try:
        product1 = input("How much does iPhone Pro Max costs?")
        if product1 == 'q':
            break

        product1 = float(product1)

        product2 = input("How much does macBook Pro costs?")
        if product2 == 'q':
            break

        product2 = float(product2)
    except ValueError:
        print("Sorry, I really need a number.")
    else:
        total = product1 + product2
        print(f"The total amount of the bill is {total} euros.")
