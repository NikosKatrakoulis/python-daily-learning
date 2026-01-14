# Make a class called User. Create two attributes called first_name and
# last_name, and then create several other attributes that are typically
# stored in a user profile. Make a method called describe_user() that
# prints a summary of the user's information. Make another method called
# greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both
# methods for each user.

class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, email, age, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.age = age
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display the personalized greeting."""
        msg = f"Hello {self.first_name} {self.last_name}, Welcome to our community."
        print(f"\n{msg}")


user01 = User('nikos', 'katrakoulis', 'nikakotra@example.com', 20, 'athens')
user01.describe_user()
user01.greet_user()

user02 = User('giannis', 'papastamatis', 'giagiapa@example.com', 45, 'patra')
user02.describe_user()
user02.greet_user()

user03 = User('elita', 'merkouri', 'elita9675@example.com', 34, 'irakleion')
user03.describe_user()
user03.greet_user()
