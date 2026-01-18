# Create a class called Store and save it in a file called store.py.
# The class should include attributes like store name and store type,
# and a method that prints a short description of the store.
# Create a second file called my_store.py.
# Import the Store class, create an instance of it, and call one
# of its methods to show that the import is working as expected.

class Store:
    """A class representing a store."""

    def __init__(self, store_name, store_type):
        """Initialize the store."""
        self.store_name = store_name.title()
        self.store_type = store_type.title()

    def describe_store(self):
        """Display a summary of the store."""
        print(f"\n{self.store_name} is a business deals with {self.store_type}.")
