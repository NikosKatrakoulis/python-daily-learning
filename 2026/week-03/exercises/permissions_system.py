# Create a class called Permissions. The class should have one attribute
# called permissions, which stores a list of strings describing
# permissions (for example: "can edit profile", "can delete account").
# Add a method called show_permissions() that prints all permissions.
# Create a class called Member that represents a basic user.
# Inside the Member class, create an attribute that is an instance
# of the Permissions class. Create an instance of Member and use the
# show_permissions() method to display the member’s permissions.

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


class Member(User):
    """Represent a member profile."""

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of permissions.
        self.permissions = Permissions()


class Permissions:

    def __init__(self, permissions=[]):
        self.permissions = permissions

    def show_permissions(self):
        """Display the permissions this member has."""
        print("\nPermissions")
        if self.permissions:
            for permission in self.permissions:
                print(f"- {permission}")
        else:
            print("This member has no permissions.")


nikos = Member('nikos', 'papadopoulos', 'giopodo234',
               'gpapa87@example.com', 'athens')
nikos.describe_user()

nikos.permissions.show_permissions()

print("\nAdding permissions...")
nikos_permissions = [
    "can edit profile",
    "can delete account",
]


nikos.permissions.permissions = nikos_permissions
nikos.permissions.show_permissions()
