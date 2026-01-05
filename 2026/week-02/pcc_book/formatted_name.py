# A function doesn’t always have to display its output directly.
# Instead, it can process some data and then return a value or
# set of values. The value the function returns is called a
# return value. The return statement takes a value from inside
# a function and sends it back to the line that called the
# function. Return values allow you to move much of your
# program’s grunt work into functions, which can simplify the
# body of your program.
# Let’s look at a function that takes a first and last name, and
# returns a neatly formatted full name:

def get_formatted_name(first_name, last_name):
    """Return a fill name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# The definition of get_formatted_name() takes as parameters
# a first and last name. The function combines these two
# names, adds a space between them, and assigns the result
# to full_name ❶. The value of full_name is converted to title
# case, and then returned to the calling line ❷.
# When you call a function that returns a value, you need to
# provide a variable that the return value can be assigned to.
# In this case, the returned value is assigned to the variable
# musician ❸. The output shows a neatly formatted name
# made up of the parts of a person’s name.

# Sometimes it makes sense to make an argument optional,
# so that people using the function can choose to provide
# extra information only if they want to. You can use default
# values to make an argument optional. This function works when
# given a first, middle, and last name. The function takes in all
# three parts of a name and then builds a string out of them. The
# function adds spaces where appropriate and converts the full name
# to title case. But middle names aren’t always needed, and this function
# as written would not work if you tried to call it with only a
# first name and a last name. To make the middle name
# optional, we can give the middle_name argument an empty
# default value and ignore the argument unless the user
# provides a value. To make get_formatted_name() work without
# a middle name, we set the default value of middle_name to an
# empty string and move it to the end of the list of
# parameters:

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('johh', 'lee', 'hooker')
print(musician)
