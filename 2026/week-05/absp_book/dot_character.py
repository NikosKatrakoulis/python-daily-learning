# The . (or dot) character in a regular expression string matches any
# character except for a newline.

import re

at_re = re.compile(r'.at')
print(at_re.findall("The cat in the hat sat on the flat mat."))

# Remember that the dot character will match just one character, which
# is why the text flat in the previous example matched only lat. To match an
# actual period, escape the dot with a backslash: \.
