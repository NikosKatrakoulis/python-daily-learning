# Write a program that asks the user to enter three numbers. Calculate and
# print their average. Use a try-except block to handle cases where the user
# enters text instead of numbers. If an error occurs, print a friendly message
# asking the user to enter valid numbers.

try:
    x = int(input("Give me a number:"))
    y = int(input("Give me a number:"))
    z = int(input("Give me a number:"))
except ValueError:
    print("Sorry, I really need a number.")
else:
    total = x + y + z
    average = total / 3
    print(f"The average of the numbers {x},{y} and {z} is {average}.")
