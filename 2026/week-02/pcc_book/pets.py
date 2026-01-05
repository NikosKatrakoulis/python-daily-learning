# When you call a function, Python must match each
# argument in the function call with a parameter in the
# function definition. The simplest way to do this is based on
# the order of the arguments provided. Values matched up
# this way are called positional arguments.
# To see how this works, consider a function that displays
# information about pets. The function tells us what kind of
# animal each pet is and the pet’s name, as shown here:

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')

# You can call a function as many times as needed. Describing
# a second, different pet requires just one more call to
# describe_pet():

describe_pet('dog', 'willie')

# You can get unexpected results if you mix up the order of
# the arguments in a function call when using positional
# arguments. In this function call, we list the name first and the type of
# animal second. Because the argument 'harry' is listed first
# this time, that value is assigned to the parameter
# animal_type. Likewise, 'hamster' is assigned to pet_name. Now
# we have a “harry” named “Hamster”.

# Keyword arguments free you from
# having to worry about correctly ordering your arguments in
# the function call, and they clarify the role of each value in
# the function call.


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# When you use keyword arguments, be sure to use the
# exact names of the parameters in the function’s
# definition.

# When you define a
# default value for a parameter, you can exclude the
# corresponding argument you’d usually write in the function
# call. Using default values can simplify your function calls
# and clarify the ways your functions are typically used.
# For example, if you notice that most of the calls to
# describe_pet() are being used to describe dogs, you can set
# the default value of animal_type to 'dog'. Now anyone calling
# describe_pet() for a dog can omit that information:


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='harry')

# Note that the order of the parameters in the function
# definition had to be changed. Because the default value
# makes it unnecessary to specify a type of animal as an
# argument, the only argument left in the function call is the
# pet’s name. Python still interprets this as a positional
# argument, so if the function is called with just a pet’s name,
# that argument will match up with the first parameter listed
# in the function’s definition. This is the reason the first
# parameter needs to be pet_name.

# This function call would have the same output as the
# previous example. The only argument provided is 'willie',
# so it is matched up with the first parameter in the definition,
# pet_name.

describe_pet('willie')

# When you use default values, any parameter with a
# default value needs to be listed after all the
# parameters that don’t have default values. This allows
# Python to continue interpreting positional arguments
# correctly.

# With this definition, an argument always needs to be
# provided for pet_name, and this value can be provided using
# the positional or keyword format. If the animal being
# described is not a dog, an argument for animal_type must be
# included in the call, and this argument can also be specified
# using the positional or keyword format.
# All of the following calls would work for this function:

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
