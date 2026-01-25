# The startswith() and endswith() methods return True if the string value on
# which they’re called begins or ends (respectively) with the string passed to
# the method; otherwise, they return False.

spam = 'Hello, world!'.startswith('Hello')
print(spam)

spam = 'Hello, world!'.endswith('world!')
print(spam)

spam = 'abc123'.startswith('abcdef')
print(spam)

spam = 'abc123'.endswith('12')
print(spam)

spam = 'Hello, world!'.startswith('Hello, world!')
print(spam)

spam = 'Hello, world!'.endswith('Hello, world!')
print(spam)

# These methods are useful alternatives to the equals operator (==) if you
# need to check only whether the first or last part of the string, rather than
# the whole thing, is equal to another string.
