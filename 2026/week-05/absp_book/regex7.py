# Sometimes you may want to match everything and anything. For example,
# say you want to match the string 'First Name:', followed by any and all text,
# followed by 'Last Name:' and any text once again. You can use the dot-star
# (.*) to stand in for that “anything.” Remember that the dot character means
# “any single character except the newline,” and the star character means
# “zero or more of the preceding character.”

import re

name_pattern = re.compile(r'First Name:(.*) Last Name:(.*)')
name_match = name_pattern.search('First Name: Al Last Name: Steigart')

print(name_match.group(1))
print(name_match.group(2))


# The dot-star uses greedy mode: it will always try to match as much text
# as possible. To match any and all text in a non-greedy or lazy fashion, use
# the dot, star, and question mark (.*?). As when it’s used with curly
# brackets, the question mark tells Python to match in a non-greedy way.


lazy_pattern = re.compile(r'<.*?>')
match1 = lazy_pattern.search('<To serve man> for dinner.')
print(match1.group())

greedy_re = re.compile(r'<.*>')
match2 = greedy_re.search('<To serve man> for dinner.>')
print(match2.group())

# Both regexes roughly translate to “Match an opening angle bracket,
# followed by anything, followed by a closing angle bracket.” But the string
# '<To serve man> for dinner.>' has two possible matches for the closing angle
# bracket. In the non-greedy version of the regex, Python matches the short
# est possible string: '<To serve man>'. In the greedy version, Python matches
# the longest possible string: '<To serve man> for dinner.>'.
