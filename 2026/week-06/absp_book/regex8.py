# Regular expressions are fine if the text pattern you need to match is simple.
# But matching complicated text patterns might require long, convoluted reg
# ular expressions. You can mitigate this complexity by telling the re .compile()
# function to ignore whitespace and comments inside the regular expression
# string. Enable this “verbose mode” by passing the variable re.VERBOSE as the
# second argument to re .compile().

# Now, instead of a hard-to-read regular expression like this:

import re

pattern = re.compile(
    r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext\.)\s*\d{2,5})?)')

# You can spread the regular expression over multiple lines and use comments
# to label its components, like this:

pattern = re.compile(r'''(
        (\d{3}|\(\d{3}\))?  # Area code
        (\s|-|\.)?  # Separator
        \d{3}   # First three digits
        (\s|-|\.)   # Separator
        \d{4}   # Last four digits
        (\s*(ext|x|ext\.)\s*\d{2,5})?   # Extersion
        )''', re.VERBOSE)
match1 = pattern.search("415-555-5555")
print(match1)

# Note how the previous example uses the triple-quote syntax (''') to
# create a multiline string so that you can spread the regular expression defi
# nition over many lines, making it much more legible.
# The comment rules inside the regular expression string are the same as
# for regular Python code: the # symbol and everything after it until the end
# of the line are ignored. Also, the extra spaces inside the multiline string
# for the regular expression are not considered part of the text pattern to be
# matched. This lets you organize the regular expression so that it’s easier
# to read.
