# You can use the caret symbol (^) at the start of a regex to indicate that
# a match must occur at the beginning of the searched text. Likewise, you
# can put a dollar sign ($) at the end of the regex to indicate that the
# string must end with this regex pattern. And you can use the ^ and $
# together to indicate that the entire string must match the regex—that
# is, it’s not enough for a match to be made on some subset of the string.
# For example, the r'^Hello' regular expression string matches strings
# that begin with 'Hello'.

import re

begins_with_hello = re.compile(r'^Hello')
match1 = begins_with_hello.search("Hello,world")
print(match1)

match2 = begins_with_hello.search("He said 'Hello.'") == None
print(match2)
