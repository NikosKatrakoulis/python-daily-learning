# Sometimes you won’t know ahead of time how many
# arguments a function needs to accept. Fortunately, Python
# allows a function to collect an arbitrary number of
# arguments from the calling statement.
# For example, consider a function that builds a pizza. It
# needs to accept a number of toppings, but you can’t know
# ahead of time how many toppings a person will want. The
# function in the following example has one parameter,
# *toppings, but this parameter collects as many arguments as
# the calling line provides:

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# The asterisk in the parameter name *toppings tells Python
# to make a tuple called toppings, containing all the values this
# function receives. The print() call in the function body
# produces output showing that Python can handle a function
# call with one value and a call with three values. It treats the
# different calls similarly. Note that Python packs the
# arguments into a tuple, even if the function receives only
# one value.


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# If you want a function to accept several different kinds of
# arguments, the parameter that accepts an arbitrary number
# of arguments must be placed last in the function definition.
# Python matches positional and keyword arguments first and
# then collects any remaining arguments in the final
# parameter.
# For example, if the function needs to take in a size for the
# pizza, that parameter must come before the parameter
# *toppings:


def make_pizza(size, *toppings):
    "Summerize the pizza we are about to make."
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# In the function definition, Python assigns the first value it
# receives to the parameter size. All other values that come
# after are stored in the tuple toppings. The function calls
# include an argument for the size first, followed by as many
# toppings as needed.
# Now each pizza has a size and a number of toppings, and
# each piece of information is printed in the proper place,
# showing size first and toppings after.
# You’ll often see the generic parameter name *args,
# which collects arbitrary positional arguments like this.
