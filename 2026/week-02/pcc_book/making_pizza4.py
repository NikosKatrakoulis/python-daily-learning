# You can tell Python to import every function in a module by
# using the asterisk (*) operator:

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# The asterisk in the import statement tells Python to copy
# every function from the module pizza into this program file.
# Because every function is imported, you can call each
# function by name without using the dot notation.
# Python may see
# several functions or variables with the same name, and
# instead of importing all the functions separately, it will
# overwrite the functions.
# The best approach is to import the function or functions
# you want, or import the entire module and use the dot
# notation. This leads to clear code that’s easy to read and
# understand. I include this section so you’ll recognize import
# statements like the following when you see them in other
# people’s code.
