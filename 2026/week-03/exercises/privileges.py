# Write a separate Privileges class. The class should have one attribute,
# privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges
# instance as an attribute in the Admin class. Create a new instance of
# Admin and use your method to show its privileges.

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
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nHello {self.username},welcome back!")

    def increment_login_attemps(self):
        """Increment the value of login_attemps."""
        self.login_attemps += 1

    def reset_login_attemps(self):
        """Reset of login_attemps to 0."""
        self.login_attemps = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges
        self.privileges = Privileges()


class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges this admninistrator has."""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


admin = Admin('giorgos', 'papadopoulos', 'giopodo234',
              'gpapa87@example.com', 'athens')
admin.describe_user()

admin.privileges.show_privileges()

print("\nAdding privileges...")
admin_privileges = ["can reset passwords",
                    "can moderate discussions",
                    "can suspend accounts",]

admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()
