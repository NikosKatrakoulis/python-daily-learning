# Computers store information as bytes (strings of binary numbers), which
# means we need to be able to convert text to numbers. Because of this
# requirement, every text character has a corresponding numeric value called
# a Unicode code point. For example, the numeric code point is 65 for 'A',
# 52 for '4', and 33 for '!'. You can use the ord() function to get the
# code point of a one-character string, and the chr() function to get
# the one-character string of an integer code point.

spam = ord('A')
print(spam)

spam = ord('4')
print(spam)

spam = ord('!')
print(spam)

spam = chr(65)
print(spam)

# These functions are useful when you need to order or perform a math
# ematical operation on characters:

spam = ord('B')
print(spam)

spam = ord('A') < ord('B')
print(spam)

spam = chr(ord('A'))
print(spam)

spam = chr(ord('A') + 1)
print(spam)
