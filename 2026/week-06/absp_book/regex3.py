# The r'\d$' regular expression string matches strings that end with a
# numeric character between 0 and 9.

import re

ends_with_number = re.compile(r'\d$')
match1 = ends_with_number.search("Your number is 42")
print(match1)

match2 = ends_with_number.search("Your number is forty two") == None
print(match2)
