# Add an attribute called login_attempts to your User class.
# Write a method called increment_login_attempts() that
# increments the value of login_attempts by 1. Write another method
# called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was
# incremented properly, and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.


class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, email, age, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.age = age
        self.location = location.title()
        self.login_attemps = 0

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

    def increment_login_attemps(self):
        """Increment the value of login_attemps."""
        self.login_attemps += 1

    def reset_login_attemps(self):
        """Reset login_attemps to 0."""
        self.login_attemps = 0


user = User('nikos', 'katrakoulis', 'nikakotra@example.com', 20, 'athens')
user.describe_user()
user.greet_user()

print(f"\nMaking 3 login attemps...")
user.increment_login_attemps()
user.increment_login_attemps()
user.increment_login_attemps()
print(f"    Login Attemps: {user.login_attemps}")

print("Resetting login attemps...")
user.reset_login_attemps()
print(f"    Login Attemps: {user.login_attemps}")
