# To make multiple characters optional, place them in a group and put
# the ? after the group. In the earlier phone number example, you can use ?
# to make the regex look for phone numbers that either do or do not have an
# area code.

import re

pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
match1 = pattern.search("My number is 415-555-4242")
print(match1.group())

match2 = pattern.search("My number is 555-4242")
print(match2.group())

# You can think of the ? as saying, “Match zero or one of the group
# preceding this question mark.” If you need to match an actual question
# mark character, escape it with \?
