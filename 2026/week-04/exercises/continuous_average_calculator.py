# Write a program that repeatedly asks the user to enter three numbers and
# calculates their average. Use a while loop so the user can continue
# entering values. Allow quitting with 'q'. Catch invalid input using
# try-except. Print a friendly error message if the user enters text
# instead of numbers.

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

        z = input("Give me a number:")
        if z == 'q':
            break

        z = int(z)
    except ValueError:
        print("Sorry, I really need a number.")
    else:
        total = x + y + z
        avg = total / 3
        print(f"\nThe average of the {x}, {y} and {z} is {avg}")
