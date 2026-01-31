# Parentheses create groups in regular expressions and are not interpreted
# as part of the text pattern. So, what do you do if you need to match a paren
# thesis in your text? For instance, maybe the phone numbers you are trying
# to match have the area code set in parentheses: '(415) 555-4242'.
# In this case, you need to escape the ( and ) characters with a backslash.
# The \( and \) escaped parentheses will be interpreted as part of the pattern
# you are matching.

import re

pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = pattern.search("My phone number is (415) 555-4242.")
print(mo.group(1))
print(mo.group(2))
