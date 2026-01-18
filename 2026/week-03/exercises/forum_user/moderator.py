from forum_user import ForumUser


class Moderator(ForumUser):
    """A class representing a moderator."""

    def __init__(self, username, email, location):
        """Initialize the moderator."""
        super().__init__(username, email, location)
        self.permissions = Permissions()


class Permissions:
    """A simple attempt to display permissions of moderator."""

    def __init__(self, permissions=[]):
        """Initialize the attribute."""
        self.permissions = permissions

    def show_permissions(self):
        """Display the permissions."""
        print("\nPermissions:")
        for permission in self.permissions:
            print(f"- {permission}")


mod = Moderator('mpampasidis', 'mpampasidis25@sample.com', 'athens')
mod.describe_user()

mod_permissions = [
    "add user",
    "add post",
    "add photo",
]

mod.permissions.permissions = mod_permissions
mod.permissions.show_permissions()
