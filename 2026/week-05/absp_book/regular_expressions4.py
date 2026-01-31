# The | character is called a pipe, and it’s used as the alternation operator
# in regular expressions. You can use it anywhere you want to match one of
# multiple expressions. For example, the regular expression r'Cat|Dog' will
# match either 'Cat' or 'Dog'. You can also use the pipe to match one of
# several patterns as part of your regex. For example, say you wanted to
# match any of the strings 'Caterpillar', 'Catastrophe', 'Catch', or
# 'Category'. Since all of these strings start with Cat, it would be
# nice if you could specify that prefix only once. You can do this by
# using the pipe within parentheses to separate the possible suffixes.

import re

pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
match = pattern.search("Catch me if you can.")
print(match.group())
print(match.group(1))

# If you need to match an actual pipe character, escape it with a backs
# lash, like \|
