# A list
# comprehension allows you to generate this same list in just
# one line of code. To use this syntax, begin with a descriptive name for the
# list, such as squares. Next, open a set of square brackets and
# define the expression for the values you want to store in the
# new list. In this example the expression is value**2, which
# raises the value to the second power. Then, write a for loop
# to generate the numbers you want to feed into the
# expression, and close the square brackets.

squares = [value ** 2 for value in range(1, 11)]
print(squares)
