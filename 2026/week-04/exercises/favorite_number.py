# Use a variable to represent your favorite number. Then, using that
# variable, create a message that reveals your favorite number. Print
# that message.

favorite_number = 27
msg = f'I was born in {favorite_number} of August 1995. '
print(msg)

msg = '%s is my favorite number.' % (favorite_number)
print(msg)

msg = '{} is my favorite number because it is my birthdate.'.format(
    favorite_number)
print(msg)
