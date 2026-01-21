# Write a program that repeatedly asks the user for two numbers and divides
# the first by the second. Wrap your code in a while loop so the user can
# keep trying even after entering invalid input. Allow the user to enter 'q'
# at any time to quit. Use try-except to handle invalid input and division
# by zero. Print the result if no error occurs.

print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("Give me a number:")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me a number:")
        if y == 'q':
            break

        y = int(y)

        remainder = x / y
    except ValueError:
        print("Sorry, I really need a number.")
    except ZeroDivisionError:
        print("Sorry I can not divide with 0. Enter a number greater than 0.")
    else:
        print(f"The result of {x} / {y} is {remainder}.")
