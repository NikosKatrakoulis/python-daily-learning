# Create a class called Features. The class should store a list of
# feature names (for example: "ad-free experience", "priority support").
# Add a method called show_features() that displays all features.
# Create a class called PremiumUser.
# Inside this class, create an attribute that holds an instance of Features.
# Create a PremiumUser instance, assign several features,
# and call the method to display them.


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


class PremiumUser(User):
    """A class represent a premium user."""

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.features = Features()


class Features:
    """A class represents a list of features."""

    def __init__(self, features=[]):
        self.features = features

    def show_feautures(self):
        print("\nFeatures:")
        if self.features:
            for feature in self.features:
                print(f"- {feature}")
        else:
            print("There are no features.")


nikos = PremiumUser('nikos', 'papadopoulos', 'giopodo234',
                    'gpapa87@example.com', 'athens')
nikos.describe_user()

nikos.features.show_feautures()

print
nikos_features = [
    "ad-free experience",
    "priority support",
]

nikos.features.features = nikos_features
nikos.features.show_feautures()
