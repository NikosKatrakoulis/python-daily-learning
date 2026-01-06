# To start importing functions, we first need to create a
# module. A module is a file ending in .py that contains the
# code you want to import into your program. Let’s make a
# module that contains the function make_pizza(). To make this
# module, we’ll remove everything from the file pizza.py
# except the function make_pizza():


import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Now we’ll make a separate file called making_pizzas.py in
# the same directory as pizza.py. This file imports the module
# we just created and then makes two calls to make_pizza().
# When Python reads this file, the line import pizza tells
# Python to open the file pizza.py and copy all the functions
# from it into this program.
# To call a function from an imported module, enter the
# name of the module you imported, pizza, followed by the
# name of the function, make_pizza(), separated by a dot ❶.
# This code produces the same output as the original program
# that didn’t import a module.
