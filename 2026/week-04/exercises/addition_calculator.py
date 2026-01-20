# Wrap your code from Exercise addition.py in a while loop so the user can
# continue entering numbers even if they make a mistake and enter text
# instead of a number.

print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number:")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me a number:")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")
    else:
        total = x + y
        print(f"The sum of {x} and {y} is {total}.")
