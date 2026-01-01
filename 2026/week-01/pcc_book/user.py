# Dictionaries can be used to store information in a
# variety of ways; therefore, several different ways exist to
# loop through them. You can loop through all of a dictionary’s
# key-value pairs, through its keys, or through its values.

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# what if you wanted to see everything stored in this
# user’s dictionary? To do so, you could loop through the
# dictionary using a for loop:

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# This code would work just as well if you
# had used abbreviations for the variable names, like this:

for k, v in user_0.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")
