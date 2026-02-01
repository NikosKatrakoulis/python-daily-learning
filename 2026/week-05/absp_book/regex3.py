# The * (called the star or asterisk) means “match zero or more.” In other
# words, the qualifier that precedes the star can occur any number of times in
# the text. It can be completely absent or repeated over and over again.

import re

pattern = re.compile('Eggs( and spam)*')
print(pattern.search('Eggs'))
print(pattern.search('Eggs and spam'))
print(pattern.search('Eggs and spam and spam'))
print(pattern.search('Eggs and spam and spam and spam'))

# While the 'Eggs' part of the string must appear once, there can be any
# number of ' and spam' following it, including zero instances.
# If you need to match an actual star character, prefix the star in the
# regular expression with a backslash, \*.
