class ForumUser:
    """A class representing a user."""

    def __init__(self, username, email, location):
        """Initialize the user."""
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user."""
        print(f"\nUsername: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
