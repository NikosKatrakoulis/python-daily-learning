# Start with a class called Library. Add two constant attributes: library_name,
# city. Add one attribute with a default value: books_lent (default value: 0)
# Create an instance of the class and print all three attributes.
# Change the value of books_lent directly and print it again.
# Add a method called set_books_lent() that allows you to set the
# total number of books lent. Call this method with a new value and
# print the result. Add a method called increment_books_lent() that
# increments the number of books lent by a given amount.
# Call this method with a number representing how many books were
# lent in one day.

class Library:
    """A class representing a library."""

    def __init__(self, library_name, city):
        """Initialize the library."""
        self.library_name = library_name.title()
        self.city = city.title()
        self.books_lent = 0

    def describe_library(self):
        """Display a summary of the library."""
        msg = f"{self.library_name} is the biggest library in {self.city}."
        print(f"\n{msg}")

    def open_library(self):
        """Display a message that the library is open."""
        msg = f"{self.library_name} is now open. Come on in!"
        print(f"\n{msg}")

    def set_books_lent(self, books_lent):
        """Allow the user to set the books have been lent."""
        self.books_lent = books_lent

    def increment_books_lent(self, additional_books):
        """Allow the user to increase the books have been lent."""
        self.books_lent += additional_books


library = Library('politeia', 'athens')
library.describe_library()

print(f"\nNumber of lent books: {library.books_lent}")
library.books_lent = 50
print(f"Number of lent books: {library.books_lent}")

library.set_books_lent(200)
print(f"Number of lent books: {library.books_lent}")

library.increment_books_lent(1000)
print(f"Number of lent books: {library.books_lent}")
