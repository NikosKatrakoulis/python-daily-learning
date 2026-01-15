# Create a class called Account. Add attributes like username and email.
# Add an attribute called password_attempts with a default value of 0.
# Write a method called increment_password_attempts() that increases
# password_attempts by 1. Write a method called reset_password_attempts()
# that resets it back to 0. Create an instance of Account, call
# increment_password_attempts() several times, and print the value to
# confirm it increases correctly. Then call reset_password_attempts()
# and print the value again to confirm it resets.

class Account:
    """A class representing an account."""

    def __init__(self, username, email):
        """Initialize the account."""
        self.username = username
        self.email = email
        self.password_attemps = 0

    def describe_account(self):
        """Display a summary of account's information."""
        print(f"\nUsername: {self.username}")
        print(f"Email: {self.email}")

    def greet_account(self):
        """Display the personalized greeting."""
        print(F"\nHello {self.username}! Welcome to your account.")

    def increment_password_attemps(self):
        """Increment the value of password_attemps."""
        self.password_attemps += 1

    def reset_password_attemps(self):
        """Reset password_attemps to 0."""
        self.password_attemps = 0


account = Account('nikokat', 'nikokat@example.com.gr')
account.describe_account()
account.greet_account()

print("\nMaking 5 password attemmps...")
account.increment_password_attemps()
account.increment_password_attemps()
account.increment_password_attemps()
account.increment_password_attemps()
account.increment_password_attemps()
print(f"    Password attemps: {account.password_attemps}")

print(f"\nResetting password attemps...")
account.reset_password_attemps()
print(f"    Password attemps: {account.password_attemps}")
