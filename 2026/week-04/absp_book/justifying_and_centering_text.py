# The rjust() and ljust() string methods return a padded version of the
# string on which they’re called, with spaces inserted to justify the text.
# The first argument to both methods is an integer length for the justified
# string.

example = 'Hello'.rjust(10)
print(example)

example = 'Hello'.rjust(20)
print(example)

example = 'Hello, World'.rjust(20)
print(example)

example = 'Hello'.ljust(10)
print(example)

# An optional second argument to rjust() and ljust() will specify a fill
# character other than a space character.

example = 'Hello'.rjust(20, '*')
print(example)

example = 'Hello'.ljust(20, '-')
print(example)

# The center() string method works like ljust() and rjust() but centers
# the text, rather than justifying it to the left or right

example = 'Hello'.center(20)
print(example)

example = 'Hello'.center(20, '=')
print(example)
