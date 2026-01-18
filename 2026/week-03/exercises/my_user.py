# Create a class called User and store it in a file called user.py.
# The class should store basic user information and include at
# least one method that prints a greeting message.
# Create a second file called my_user.py.
# Import the User class, create an instance of it, and call one
# of its methods to verify that the import works correctly.

from users import User

nikos = User('nikos', 'katrakoulis', 'nikkat@sample.com', 30, 'athens')
nikos.greet_user()
