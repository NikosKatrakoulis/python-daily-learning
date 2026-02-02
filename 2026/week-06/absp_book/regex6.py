# Normally, regular expressions match text with the exact casing you specify.
# For example, the following regexes match completely different strings:

import re

pattern1 = re.compile('RoboCop')
pattern2 = re.compile('ROBOCOP')
pattern3 = re.compile('robOcop')
pattern4 = re.compile('RobocOp')

print(pattern1)
print(pattern2)
print(pattern3)
print(pattern4)


# But sometimes you care only about matching the letters, and aren’t
# worried about whether they’re uppercase or lowercase. To make your regex
# case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to
# re .compile()

pattern = re.compile(r'robocop', re.I)
match1 = pattern.search("Robocop is part man, part machine, all cop.").group()
print(match1)

match2 = pattern.search("ROBOCOP protects the innocent.").group()
print(match2)

match3 = pattern.search("Have you seen robocop").group()
print(match3)

# The regular expression now matches strings with any casing.
