# A moderator is a special kind of user. Create a class called Moderator
# that inherits from a User class. Add an attribute called permissions
# that stores a list of strings such as "can edit comments",
# "can delete comments", "can mute users". Write a method called
# show_permissions() that displays all the moderator’s permissions.
# Create an instance of Moderator, assign at least three permissions,
# and call the method to display them.

class User:
    """A class representing a simple user's profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attemps = 0

    def describe_user(self):
        """Display the summary of a user."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display a personalized message."""
        print(f"\nHello {self.first_name} {self.last_name}, welcome back.")

    def increment_login_attemps(self):
        """Increment the login_attemps."""
        self.login_attemps += 1

    def reset_login_attemps(self):
        """Reset the login_attemps to 0."""
        self.login_attemps = 0


class Moderator(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.permissions = []

    def show_permissions(self):
        """Display the permissions this moderator has."""
        print("\nShowing all the permissions:")
        for permission in self.permissions:
            print(f"- {permission}")


moderator = Moderator('giorgos', 'papadopoulos', 'giopodo234',
                      'gpapa87@example.com', 'athens')
moderator.describe_user()

moderator.permissions = [
    "can edit comments",
    "can delete comments",
    "can mute users",
]

moderator.show_permissions()
