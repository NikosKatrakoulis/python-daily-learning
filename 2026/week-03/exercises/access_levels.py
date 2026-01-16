# Create a class called AccessLevels. The class should have one attribute
# that stores a list of access levels (for example: "read", "write", "execute").
# Add a method called show_access_levels() that prints all access levels.
# Create a class called SystemUser. Inside SystemUser, create an attribute
# that is an instance of AccessLevels.Create an instance of SystemUser,
# assign several access levels, and display them using the appropriate method.

class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attemps = 0

    def describe_user(self):
        """Display a summary of user's information"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display a personalized message to the user."""
        print(f"Hello {self.username}, welcome back!")

    def increment_login_attemps(self):
        """Increment the value of login_attemps."""
        self.login_attemps += 1

    def reset_login_attemps(self):
        """Reset of login_attemps to 0."""
        self.login_attemps = 0


class SystemUser(User):
    """A class representing a system user."""

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.access_levels = AccessLevels()


class AccessLevels:
    """A class representing the access levels."""

    def __init__(self, access_levels=[]):
        """Initialize the access levels."""
        self.access_levels = access_levels

    def show_access_levels(self):
        """Display the access levels."""
        print("\nAccess Levels:")
        if self.access_levels:
            for access_level in self.access_levels:
                print(f"- {access_level}")
        else:
            print("There are no access levels.")


nikos = SystemUser('nikos', 'papadopoulos', 'giopodo234',
                   'gpapa87@example.com', 'athens')
nikos.describe_user()

nikos.access_levels.show_access_levels()

nikos_access_levels = [
    "read",
    "write",
    "execute",
]

nikos.access_levels.access_levels = nikos_access_levels
nikos.access_levels.show_access_levels()
