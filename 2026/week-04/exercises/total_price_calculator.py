# Write a program that asks the user to enter the price of two products.
# Add the prices together and print the total cost. Use try-except to handle
# cases where the user enters invalid input (text instead of numbers).
# Print a clear error message if conversion fails.

try:
    product1 = float(input("How much does iPhone costs?"))
    product2 = float(input("How much does macBook Pro costs?"))
except ValueError:
    print("Sorry, I really need a number.")
else:
    total = product1 + product2
    print(f"First product: {product1}")
    print(f"Second product: {product2}")
    print(f"Total amount: {total}")
