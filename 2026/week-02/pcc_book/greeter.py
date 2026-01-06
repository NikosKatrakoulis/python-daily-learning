# Here’s a simple function named greet_user() that prints a
# greeting:

def greet_user():
    """Display a simple greeting."""
    print("Hello!")


greet_user()

# This example shows the simplest structure of a function.
# The first line uses the keyword def to inform Python that
# you’re defining a function. This is the function definition,
# which tells Python the name of the function and, if
# applicable, what kind of information the function needs to
# do its job. The parentheses hold that information. In this
# case, the name of the function is greet_user(), and it needs
# no information to do its job, so its parentheses are empty.
# (Even so, the parentheses are required.) Finally, the
# definition ends in a colon.

# If you modify the function greet_user() slightly, it can greet
# the user by name. For the function to do this, you enter
# username in the parentheses of the function’s definition at def
# greet_user(). By adding username here, you allow the function
# to accept any value of username you specify. The function now
# expects you to provide a value for username each time you
# call it. When you call greet_user(), you can pass it a name,
# such as 'jesse', inside the parentheses:


def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user('jesse')


# You can use functions with all the Python structures you’ve
# learned about so far. For example, let’s use the
# get_formatted_name() function with a while loop to greet users
# more formally. Here’s a first attempt at greeting people
# using their first and last names.

# We want the user to be
# able to quit as easily as possible, so each prompt should
# offer a way to quit. The break statement offers a
# straightforward way to exit the loop at either prompt:

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# This is a while loop
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello {formatted_name}!")
