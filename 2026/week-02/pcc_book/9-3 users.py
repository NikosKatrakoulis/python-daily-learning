# Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically
# stored in a user profile. Make a method called describe_user() that prints a
# summary of the user’s information. Make another method called greet_user()
# that prints a personalized greeting to the user.
# Create several instances representing different users, and call both
# methods for each user.

class User:
    """Represent a simple user profile"""

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""

        print(f"\nWelcome back, {self.username}!")


nikos = User('nikos', 'katrakoulis', 'niko_kat',
             'nkatrakoulis@pccexercise.com', 'megara')
nikos.describe_user()
nikos.greet_user()

giorgos = User('giorgos', 'papadopoulos', 'gpapa',
               'gpapadopoulos@hotmail.com', 'nyc')
giorgos.describe_user()
giorgos.greet_user()
