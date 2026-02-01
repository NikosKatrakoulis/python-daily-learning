# Python’s regular expressions are greedy by default, which means that
# in ambiguous situations, they will match the longest string possible. The
# non-greedy(also called lazy) version of the curly brackets, which matches
# the shortest string possible, must follow the closing curly bracket with a
# question mark.

import re

greedy_pattern = re.compile(r'(Ha){3,5}')
match1 = greedy_pattern.search('HaHaHaHaHa')
print(match1.group())

lazy_pattern = re.compile(r'(Ha){3,5}?')
match2 = lazy_pattern.search('HaHaHaHaHa')
print(match2.group())

# Note that the question mark can have two meanings in regular expres
# sions: declaring a lazy match or declaring an optional qualifier. These
# meanings are entirely unrelated.
