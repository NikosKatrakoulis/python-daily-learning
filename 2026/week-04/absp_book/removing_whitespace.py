# Sometimes you may want to strip off whitespace characters (spaces, tabs,
# and newlines) from the left side, right side, or both sides of a string. The
# strip() string method will return a new string without any whitespace char
# acters at the beginning or end, while the lstrip() and rstrip() methods will
# remove whitespace characters from the left and right ends, respectively.

spam = '    Hello, World    '
print(spam.strip())

print(spam.lstrip())

print(spam.rstrip())

# Optionally, a string argument will specify which characters on the ends
# to strip.

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

# Passing strip() the argument 'ampS' will tell it to strip occurrences of a,
# m, p, and S from the ends of the string stored in spam. The order of the char
# acters in the string passed to strip() doesn’t matter: strip('ampS') will do the
# same thing as strip('mapS') or strip('Spam').
