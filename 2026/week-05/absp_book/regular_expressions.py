# Regular expressions can be much more sophisticated than this one. For
# example, adding a numeral, such as 3, in curly brackets ({3}) after a
# pattern is like saying, “Match this pattern three times.” So the slightly
# shorter regex r'\d{3}-\d{3}-\d{4}' also matches the phone number pattern.
# Note that we often write regex strings as raw strings, with the r prefix.
# This is useful, as regex strings often have backslashes. Without using raw
# strings, we would have to enter expressions such as'\\d'.

import re

phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search("My number is 415-555-4242")
print(match_obj.group())
