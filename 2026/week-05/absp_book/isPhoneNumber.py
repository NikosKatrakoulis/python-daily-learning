# Say you want to find a US phone number in a string; you’re looking for
# three numbers, a hyphen, three numbers, a hyphen, and four numbers.
# Here’s an example: 415-555-4242.
# Let’s write a function named is_phone_number() to check whether a string
# matches this pattern and return either True or False.

def is_phone_number(text):
    if len(text) != 12:  # Phone numbers have exactly 12 characters.
        return False
    for i in range(0, 3):  # The first three characters must be numbers.
        if not text[i].isdecimal():
            return False
    if text[3] != '-':  # The fourth character must be a dash.
        return False
    for i in range(4, 7):  # The next three characters must be numbers.
        if not text[i].isdecimal():
            return False
    if text[7] != '-':  # The eighth character must be a dash.
        return False
    for i in range(8, 12):  # The next four characters must be numbers.
        if not text[i].isdecimal():
            return False
    return True


# print('Is 415-555-4242 a phone number?')
# print(is_phone_number('415-555-4242'))     True
# print('Is Moshi moshi a phone number?')
# print(is_phone_number('Moshi moshi'))     False

# If you wanted to find a phone number within a larger string, you would
# have to add even more code to locate the pattern.

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    segment = message[i:i+12]
    if is_phone_number(segment):
        print('Phone number found: ' + segment)
print('Done')

# On each iteration of the for loop, a new segment of 12 characters from
# message is assigned to the variable segment 1. For example, on the first
# iteration, i is 0, and segment is assigned message[0:12]
# (that is, the string 'Call me at 4'). On the next iteration, i is 1, and
# segment is assigned message[1:13]  (the string 'all me at 41').
# In other words, on each iteration of the for loop, segment takes on the
# following values:
# 'Call me at 4'
# 'all me at 41'
# 'll me at 415'
# 'l me at 415-'
# and so on, until its last value is 's my office.'
# The loop’s code passes segment to is_phone_number() to check whether
# it matches the phone number pattern 2, and if so, it prints the segment.
# Once it has finished going through message, we print Done.
# While the string in message is short in this example, the program would
# run in less than a second even if it were millions of characters long.
# A similar program that finds phone numbers using regular expressions would
# also run in less than a second; however, regular expressions make writing
# these programs much quicker.
