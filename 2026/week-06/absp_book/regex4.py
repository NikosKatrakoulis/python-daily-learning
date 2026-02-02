# The r'^\d+$' regular expression string matches strings that both begin
# and end with one or more numeric characters.

import re

whole_string_is_num = re.compile(r'^\d+$')
match1 = whole_string_is_num.search("1234567890")
print(match1)

match2 = whole_string_is_num.search("12345xyz67890") == None
print(match2)
