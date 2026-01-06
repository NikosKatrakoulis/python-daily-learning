# You can also import a specific function from a module.
# You can import as many functions as you want from a
# module by separating each function’s name with a comma.
# With this syntax, you don’t need to use the dot notation
# when you call a function. Because we’ve explicitly imported
# the function make_pizza() in the import statement, we can call
# it by name when we use the function.

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
