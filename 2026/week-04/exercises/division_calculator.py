# Write a program that asks the user for two numbers and divides the first
# number by the second. Use try-except blocks to catch: invalid numerical
# input ,division by zero. Print a friendly error message in each case.
# If no error occurs, print the result of the division.

try:
    x = input("Give me a number:")
    x = int(x)

    y = input("Give me a number:")
    y = int(y)
    remainder = x / y

except ZeroDivisionError:
    print("Sorry, I can not divide with 0.")
except ValueError:
    print("Sorry, I really need a number.")
else:
    print(f"The result of {x} / {y} is {remainder}.")
