# While * means “match zero or more,” the + (or plus) means “match one or
# more.” Unlike the star, which does not require its qualifier to appear in
# the matched string, the plus requires the qualifier preceding it to appear
# at least once. It is not optional.

import re

pattern = re.compile('Eggs( and spam)+')
print(pattern.search('Eggs and spam'))
print(pattern.search('Eggs and spam and spam'))
print(pattern.search('Eggs and spam and spam and spam'))

# The regex 'Eggs( and spam)+' will not match the string 'Eggs', because
# the plus sign requires at least one ' and spam'.
# You’ll often use parentheses in your regex strings to group together
# qualifiers so that a quantifier can apply to the entire group. For example,
# you could match any combination of dots and dashes of Morse code with
# r'(\.|\-)+' (though this expression would also match invalid Morse code
# combinations). If you need to match an actual plus sign character, prefix
# the plus sign with a backslash to escape it: \+.
