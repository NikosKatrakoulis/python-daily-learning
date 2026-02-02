# You can also use \b to make a regex pattern match only on a word
# boundary: the start of a word, end of a word, or both the start
# and end of a word. In this case, a “word” is a sequence of letters
# separated by non-letter characters. For example, r'\bcat.*?\b' matches
# a word that begins with 'cat' followed by any other characters up to
# the next word boundary:

import re

pattern = re.compile(r'\bcat.*?\b')
match1 = pattern.findall("The cat found a catapult catalog in the catacombs.")
print(match1)

# The \B syntax matches anything that is not a word boundary.

pattern = re.compile(r'\Bcat\B')
match2 = pattern.findall('certificate')  # Match
match3 = pattern.findall('catastrophe')  # No match

print(match2)
print(match3)

# It is useful for finding matches in the middle of a word.
