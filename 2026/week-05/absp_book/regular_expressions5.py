# In addition to a search() method, Pattern objects have a findall() method.
# While search() will return a Match object of the first matched text in the
# searched string, the findall() method will return the strings of every match
# in the searched string. There is one detail you need to keep in mind when
# using findall(). The method returns a list of strings as long as there are
# no groups in the regular expression.

import re

pattern = re.compile(r'\d{3}-\d{3}-\d{4}')  # This regex has no groups.
print(pattern.findall("Cell:415-555-9999 Workd: 212-555-0000"))

# If there are groups in the regular expression, then findall() will return
# a list of tuples. Each tuple represents a single match, and the tuple has
# strings for each group in the regex.

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # This regex has no groups.
print(pattern.findall("Cell:415-555-9999 Workd: 212-555-0000"))

# Also keep in mind that findall() doesn’t overlap matches. For example,
# matching three numbers with the regex string r'\d{3}' matches the first
# three numbers in '1234' but not the last three:

pattern = re.compile(r'\d{3}')
print(pattern.findall("1234"))  # ["123"]
print(pattern.findall("12345"))  # ["123"]
print(pattern.findall("123456"))  # ["123","456"]
