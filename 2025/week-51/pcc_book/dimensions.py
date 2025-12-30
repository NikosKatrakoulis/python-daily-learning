# A tuple looks just like a list, except you use parentheses
# instead of square brackets. Python refers to values that cannot change as immutable,
# and an immutable list is called a tuple.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# This code tries to change the value of the first dimension,
# but Python returns a type error. Because we’re trying to
# alter a tuple, which can’t be done to that type of object.

# dimensions[0] = 250
# print(dimensions[0])
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)


# Although you can’t modify a tuple, you can assign a new
# value to a variable that represents a tuple. The first four lines define the original tuple and print the
# initial dimensions. We then associate a new tuple with the
# variable dimensions, and print the new values. Python doesn’t
# raise any errors this time, because reassigning a variable is
# valid.

dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)
