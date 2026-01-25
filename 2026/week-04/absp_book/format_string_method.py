# You can use a pair of curly brackets to mark where to insert
# the strings, just like with string interpolation.

name = 'Al'
age = 4000
message = 'Hello, my name is {}. I am {} years old.' .format(name, age)
message += '\nIn ten years I will be {}.' .format(age + 10)
print(message)

# The format() method has a few more features than %s string interpola
# tion. You can put the index integer (starting at 0) inside the curly brackets
# to note which of the arguments to format() should be inserted. This is help
# ful when inserting strings multiple times or out of order:

name = 'Al'
age = 4000
msg = '{1} years ago, {0} was born and named {0}.' .format(name, age)
print(msg)

# Most programmers prefer f-strings over these two alternatives, but you
# should learn them anyway, as you may run into them in existing code.
