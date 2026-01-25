# Versions of Python before 3.6 had other ways to put strings inside other
# strings. The first is string interpolation, in which strings included a %s
# format specifier that Python would replace with another string. For
# example, enter the following into the interactive shell:

name = 'Al'
age = 4000
message = 'Hello, my name is %s. I am %s years old.' % (name, age)
message += ' In ten years I will be %s.' % (age + 10)
print(message)

# Python will replace the first %s with the first value in the parentheses
# after the string, the second %s with the second string, and so on.
