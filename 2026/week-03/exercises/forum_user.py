# Create a module called forum_user.py. Inside this module, store
# the following classes: ForumUser, Moderator (inherits from ForumUser),
# Permissions (stores a list of permissions). The Moderator class should
# have a Permissions object as an attribute.
# Create a separate file called my_forum_user.py.
# Import the Moderator class, create an instance, assign several permissions,
# and call the method that displays them to verify that the import works.

class ForumUser:
    """A class representing a forum user."""

    def __init__(self, username, email, location):
        """Initialize the user."""
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user."""
        msg = f"Hello {self.username}, welcome back!"
        print(msg)


class Moderator(ForumUser):
    """A class representing a moderator."""

    def __init__(self, username, email, location):
        """Initialize the moderator"""
        super().__init__(username, email, location)
        self.permissions = Permissions()


class Permissions:
    """A simple attempt to represent a list of permissions."""

    def __init__(self, permissions=[]):
        """Initialize the attribute."""
        self.permissions = permissions

    def show_permissions(self):
        """Print the permissions."""
        print("\nPermissions:")
        for permision in self.permissions:
            print(f"- {permision}")
