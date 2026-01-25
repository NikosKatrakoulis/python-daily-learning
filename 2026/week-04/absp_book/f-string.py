# Putting strings inside other strings is a common operation in programming.
# So far, we’ve been using the + operator and string concatenation to do this:

name = 'Al'
age = 4000
message = 'Hello, my name is ' + name + '. I am ' + str(age) + ' years old.'
message += '\nIn ten years I will be ' + str(age + 10)
print(message)

# However, this requires a lot of tedious typing. A simpler approach is to
# use f-strings, which let you place variable names or entire expressions within
# a string. Like the r prefix in raw strings, f-strings have an f prefix before the
# starting quotation mark. Enter the following into the interactive shell:

name = 'Al'
age = 4000
message = f'Hello, my name is {name}. I am {age} years old.'
message += f'\nIn ten years I will be {age + 10}.'
print(message)
