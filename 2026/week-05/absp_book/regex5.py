# If you have a group that you want to repeat a specific number of times,
# follow the group in your regex with a number in curly brackets. For example,
# the regex (Ha){3} will match the string 'HaHaHa' but not 'HaHa', since the
# latter has only two repeats of the (Ha) group. Instead of one number, you
# can specify a range by writing a minimum, a comma, and a maximum in between
# the curly brackets. For example, the regex (Ha){3,5} will match 'HaHaHa',
# 'HaHaHaHa', and 'HaHaHaHaHa'. You can also leave out the first or second
# number in the curly brackets to keep the minimum or maximum unbounded.
# For example, (Ha){3,} will match three or more instances of the (Ha) group,
# while (Ha){,5} will match zero to five instances. Curly brackets can help
# make your regular expressions shorter.

import re

haRegex = re.compile(r'(Ha){3}')
match1 = haRegex.search('HaHaHa')
print(match1.group())

match = haRegex.search('HaHa')
print(match == None)

# Here, (Ha){3} matches 'HaHaHa' but not 'Ha'. Because it doesn’t match
# 'HaHa', search() returns None.
# The syntax of the curly bracket quantifier is similar to Python’s slice
# syntax (such as 'Hello, world!'[3:5], which evaluates to 'lo'). But there are
# key differences. In the regex quantifier, the two numbers are separated by
# a comma and not a colon. Also, the second number in the quantifier is
# inclusive: '(Ha){3,5}' matches up to and including five instances of the
# '(Ha)' qualifier.
