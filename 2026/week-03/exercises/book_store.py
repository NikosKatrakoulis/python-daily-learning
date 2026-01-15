# A bookstore is a specific kind of store. Create a class called Store
# with attributes like store_name and store_type, and a method called
# describe_store(). Then create a class called Bookstore that inherits
# from Store. Add an attribute called genres that stores a list of book
# genres the bookstore sells. Write a method called show_genres() to
# display the genres. Create an instance of Bookstore, add at least
# three genres, and call both methods.

class Store:
    """A class representing a store."""

    def __init__(self, store_name, store_type):
        """Initialize the store."""
        self.store_name = store_name.title()
        self.store_type = store_type

    def describe_store(self):
        """Display a summary of the store."""
        msg = f"{self.store_name} is a {self.store_type}."
        print(f"\n{msg}")


class BookStore(Store):
    """A class representing a book store."""

    def __init__(self, store_name, store_type='book store'):
        """Initialize the book store."""
        super().__init__(store_name, store_type)
        self.genres = []

    def show_genres(self):
        """Display the book genres."""
        print("\nWe have the following genres in our book store:")
        for genre in self.genres:
            print(f"- {genre}")


politeia = BookStore('politeia')
politeia.genres = ['classical', 'crime', 'sciFi']

politeia.describe_store()
politeia.show_genres()
