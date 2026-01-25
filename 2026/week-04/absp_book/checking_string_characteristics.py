# Along with islower() and isupper(), several other string methods have
# names beginning with the word is. These methods return a Boolean value
# that describes the nature of the string. Here are some common isX()
# string methods:

# isalpha() Returns True if the string consists only of letters and isn’t
# blank

# isalnum() Returns True if the string consists only of letters and numbers
# (alphanumerics) and isn’t blank

# isdecimal()    Returns True if the string consists only of numeric charac
# ters and isn’t blank

# isspace()    Returns True if the string consists only of spaces, tabs,
# and newlines and isn’t blank

# istitle()    Returns True if the string consists only of words that begin
# with an uppercase letter followed by only lowercase letters

spam = 'hello'.isalpha()
print(spam)

spam = 'hello123'.isalpha()
print(spam)

spam = 'hello123'.isalnum()
print(spam)

spam = 'hello'.isalnum()
print(spam)

spam = '123'.isdecimal()
print(spam)

spam = '     '.isspace()
print(spam)

spam = 'This Is Title Case'.istitle()
print(spam)
