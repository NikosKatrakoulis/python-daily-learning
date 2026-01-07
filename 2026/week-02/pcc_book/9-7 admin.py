# Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or
# Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
# strings like "can add post", "can delete post", "can ban user", and so on. Write a
# method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

class User:
    """Represent a simple user profile"""

    def __init__(self, first_name, last_name, username, email, location):
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

        print(f"\nWelcome back, {self.username}!")

    def increment_login_attemps(self):
        """Increment the value of login_attemps."""
        self.login_attemps += 1

    def reset_login_attemps(self):
        """Rest login_attemps to 0."""
        self.login_attemps = 0


class Admin(User):
    """A user with administrative privileges"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin('user', 'katrakoulis', 'niko_kat',
              'nkatrakoulis@pccexercise.com', 'megara')
admin.describe_user()


admin.privileges = [
    'can add post',
    'can delete post',
    'can ban user',
]

admin.show_privileges()
