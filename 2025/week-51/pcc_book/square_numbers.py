# We start with an empty list called squares. Then, we tell
# Python to loop through each value from 1 to 10 using the
# range() function. Inside the loop, the current value is raised
# to the second power and assigned to the variable square ❶.
# Each new value of square is then appended to the list squares
# ❷. Finally, when the loop has finished running.
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# You can use either of these approaches when you’re
# making more complex lists. Sometimes using a temporary
# variable makes your code easier to read; other times it
# makes the code unnecessarily long. Focus first on writing
# code that you understand clearly, and does what you want it
# to do. Then look for more efficient approaches as you review
# your code.


# You can easily find the minimum,
# maximum, and sum of a list of numbers.
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
