# What if you want to use re.VERBOSE to write comments in your regular
# expression, but also want to use re.IGNORECASE to ignore capitalization?
# Unfortunately, the re .compile() function takes only a single value as its
# second argument.You can get around this limitation by combining the
# re.IGNORECASE, re.DOTALL, and re.VERBOSE variables using the pipe character
# (|), which in this context is known as the bitwise or operator. For example,
# if you want a regular expression that is case-insensitive and includes
# newlines to match the dot character, you would form your re .compile()
# call like this:

import re

some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL)

# Including all three options in the second argument looks like this:

some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
match1 = some_regex.search("I will go at a concert of Foo-Fighters!")
print(match1)
# This syntax is a little old-fashioned and originates from early versions
# of Python.
