# The join() method is useful when you have a list of strings that need to
# be joined together into a single string value. We call the join() method
# on a string and pass it a list of strings, and it returns the
# concatenation of each string in the passed-in list.

example = ', '.join(['cats', 'rats', 'bats'])
print(example)

example = ' '.join(['My', 'name', 'is', 'Simon'])
print(example)

example = 'ABC'.join(['My', 'name', 'is', 'Simon'])
print(example)

# Notice that the string on which join() is called is inserted between each
# string of the list argument. For example, when we call join(['cats', 'rats',
# 'bats']) on the ', ' string, it returns the string 'cats, rats, bats'.
# Remember that we call join() on a string value and pass it a list value.

# The split() method works the opposite way: we call it on a string value,
# and it returns a list of strings.

name = 'My name is Simon'.split()
print(name)

# By default, the method splits the string 'My name is Simon' wherever it finds
# whitespace such as the space, tab, or newline characters. These whitespace
# characters aren’t included in the strings in the returned list. You can pass
# a delimiter string to the split() method to specify a different string to split
# upon.

name = 'MyABCnameABCisABCSimon'.split('ABC')
print(name)

name = 'My name is Simon'.split('m')
print(name)

# A common use of split() is to split a multiline string along the newline
# characters.

spam = '''Dear Alice,
... There is a milk bottle in the fridge
... that is labeled "Milk Experiment."
...
... Please do not drink it.
... Sincerely,
... Bob'''

print(spam.split('\n'))

# Passing split() the argument '\n' lets us split the multiline string stored
# in spam along the newlines and return a list in which each item corresponds
# to one line of the string.
