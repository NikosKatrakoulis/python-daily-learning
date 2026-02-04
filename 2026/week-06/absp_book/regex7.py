# Regular expressions don’t merely find text patterns; they can also substitute
# new text in place of those patterns. The sub() method for Pattern objects
# accepts two arguments. The first is a string that should replace any matches.
# The second is the string of the regular expression. The sub() method
# returns a string with the substitutions applied.

import re

agent_pattern = re.compile(r'Agent\w+')
match1 = agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob.')
print(match1)

# Sometimes you may need to use the matched text itself as part of the
# substitution. In the first argument to sub(), you can include \1, \2, \3,
# and so on, to mean “Enter the text of group 1, 2, 3, and so on, in the
# substitution.” This syntax is called a back reference.

# For example, say you want to censor the names of the secret agents by
# showing just the first letters of their names. To do this, you could use the
# regex Agent (\w)\w* and pass r'\1****' as the first argument to sub():

agent_pattern = re.compile(r'Agent (\w)\w*')
match2 = agent_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.')
print(match2)

# The \1 in the regular expression string is replaced by whatever text was
# matched by group 1—that is, the (\w) group of the regular expression.
