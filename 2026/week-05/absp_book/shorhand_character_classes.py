# Shorthand character class  Represents . . .

# \d                         Any numeric digit from 0 to 9 .
# \D                         Any character that is not a numeric digit from 0 to 9 .
# \w                         Any letter, numeric digit, or the underscore character .
#                            (Think of this as matching “word” characters .)

# \W                         Any character that is not a letter, numeric digit, or the
#                            underscore character .

# \s                         Any space, tab, or newline character . (Think of this as
#                            matching “space” characters .)

# \S                         Any character that is not a space, tab, or newline
#                            character


# Note that while \d matches digits and \w matches digits, letters, and the
# underscore, there is no shorthand character class that matches only letters.
# Though you can use the [a-zA-Z] character class, this character class won’t
# match accented letters or non-Roman alphabet letters such as 'é'. Also,
# remember to use raw strings to escape the backslash: r'\d'.

import re

pattern = re.compile(r'\d+\s\w+')
print(pattern.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,"
                      " 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"))

# The regular expression \d+\s\w+ will match text that has one or more
# numeric digits (\d+), followed by a whitespace character (\s), followed by
# one or more letter/digit/underscore characters (\w+). The findall() method
# returns all matching strings of the regular expression pattern in a list.
