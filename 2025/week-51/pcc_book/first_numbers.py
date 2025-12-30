for value in range(1, 5):
    print(value)
print("\n")


# You can also pass range() only one argument, and it will
# start the sequence of numbers at 0.
for value in range(6):
    print(value)


# In the example in the previous section, we simply printed
# out a series of numbers. We can use list() to convert that
# same set of numbers into a list
numbers = list(range(6))
print(numbers)
