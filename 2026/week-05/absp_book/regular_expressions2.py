# Say you want to separate one smaller part of the matched text, such as the
# area code, from the rest of the phone number. Adding parentheses will create
# groups in the regex string: r'(\d\d\d)-(\d\d\d-\d\d\d\d)'.
# Then, you can use the group() method of Match objects to grab the matching
# text from just one group. The first set of parentheses in a regex string
# will be group 1. The second set will be group 2. By passing the integer
# 1 or 2 to the group() method, you can grab different parts of the matched
# text. Passing 0 or nothing to the group() method will return the entire
# matched text.

import re

phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search("My number is 415-555-4242.")
print(mo.group(1))  # Returns the first group of the matched text

print(mo.group(2))  # Returns the second group of the matched text

print(mo.group(0))  # Returns the full matched text

print(mo.group())  # Also returns the full matched text

# If you would like to retrieve all the groups at once, use the groups()
# method (note the plural form in the name):

mo.groups()
area_code, main_number = mo.groups()
print(area_code)
print(main_number)
