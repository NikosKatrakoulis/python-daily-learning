# You can define a single character to match, as we’ve done in the
# previous examples, you can also define a set of characters to match
# inside square brackets. This set is called a character class. For example,
# the character class [aeiouAEIOU] will match any vowel, both lowercase and
# uppercase. It’s the equivalent of writing a|e|i|o|u|A|E|I|O|U, but it’s
# easier to type.

import re
vowel_pattern = re.compile(r'[aeiouAEIOU]')
print(vowel_pattern.findall("RoboCop eats BABY FOOD"))

# You can also include ranges of letters or numbers by using a hyphen.
# For example, the character class [a-zA-Z0-9] will match all lowercase letters,
# uppercase letters, and numbers. Note that, inside the square brackets, the
# normal regular expression symbols are not interpreted as such. This means
# you do not need to escape characters such as parentheses inside the square
# brackets if you want to match literal parentheses. For example, the character
# class [()] will match either an open or close parenthesis. You do not need
# to write this as [\(\)].


# By placing a caret character (^) just after the character class’s opening
# bracket, you can make a negative character class. A negative character class
# will match all the characters that are not in the character class.

consonant_pattern = re.compile(r'[^aeiouAEIOU]')
print(consonant_pattern.findall("RoboCop eats BABY FOOD"))

# Now, instead of matching every vowel, we’re matching every character
# that isn’t a vowel. Keep in mind that this includes spaces, newlines,
# punctuation characters, and numbers.
