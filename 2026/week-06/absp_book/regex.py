# The dot in .* will match everything except a newline. By passing re.DOTALL
# as the second argument to re .compile(), you can make the dot character
# match all characters, including the newline character.

import re

no_newline_re = re.compile('.*')
match1 = no_newline_re.search(
    "Serve the public trust.\nProtect the innocent.\nUphold the law.").group()
print(match1)

newline_re = re.compile('.*', re.DOTALL)
match2 = newline_re.search(
    "Serve the public trust.\nProtect the innocent.\nUphold the law.").group()
print(match2)

# The regex no_newline_re, which did not have re.DOTALL passed to the
# re .compile() call that created it, will match everything only up to the first
# newline character, whereas newline_re, which did have re.DOTALL passed to
# re .compile(), matches everything. This is why the newline_re.search() call
# matches the full string, including its newline characters.
