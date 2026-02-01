# Sometimes you may want to match a pattern only optionally. That is, the
# regex should match zero or one of the preceding qualifiers. The ? character
# flags the preceding qualifier as optional.

import re

pattern = re.compile(r'42!?')
print(pattern.search('42!'))
print(pattern.search('42'))

# The ? part of the regular expression means that the pattern ! is optional.
# So it matches both 42! (with the exclamation mark) and 42 (without it).
# As you’re beginning to see, regular expression syntax’s reliance on sym
# bols and punctuation makes it tricky to read: the ? question mark has mean
# ing in regex syntax, but the ! exclamation mark doesn’t. So r'42!?' means
# '42' optionally followed by a '!', but r'42?!' means '4' optionally followed
# by '2' followed by '!':

pattern = re.compile(r'42?!')
print(pattern.search('42!'))
print(pattern.search('4!'))
print(pattern.search('42') == None)
