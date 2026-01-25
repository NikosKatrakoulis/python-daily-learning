# The isupper() and islower() methods will return a Boolean True value if
# the string has at least one letter and all the letters are uppercase or lower
# case, respectively. Otherwise, the method returns False.

spam = 'Hello, world!'
print(spam.isupper())  # False
print(spam.islower())  # False

spam = 'HELLO'
print(spam.isupper())  # True

spam = 'abc12345'.islower()
print(spam)  # True

spam = '12345'.islower()
print(spam)  # False

spam = '12345'.isupper()
print(spam)  # False

# Since the upper() and lower() string methods themselves return strings,
# you can call string methods on those returned string values as well:

spam = 'Hello'.upper()
print(spam)

spam = 'Hello'.upper().lower()
print(spam)

spam = 'Hello'.upper().lower().upper()
print(spam)

spam = 'HELLO'.lower()
print(spam)

spam = 'HELLO'.lower().islower()
print(spam)
