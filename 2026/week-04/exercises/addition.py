# One common problem when prompting for numerical input occurs when people
# provide text instead of numbers. When you try to convert the input to
# an int, you'll get a ValueError. Write a program that prompts for two
# numbers. Add them together and print the result. Catch the ValueError
# if either input value is not a number, and print a friendly error message.
# Test your program by entering two numbers and then by entering some
# text instead of a number.

try:
    x = input("Give me a number:")
    x = int(x)

    y = input("Give me a number:")
    y = int(y)
except ValueError:
    print("Sorry, I really needed a number.")
else:
    total = x + y
    print(f"The total of {x} and {y} is {total}.")
