# Make a class called Book.
# The __init__() method should store two attributes: title and author.
# Add a method called describe_book() that prints the book’s title and author.
# Add a method called read_book() that prints a message indicating the book
# is being read. Create an instance of Book. Print both attributes
# individually, and then call both methods.


class Book:
    """A class representing a book."""

    def __init__(self, title, author):
        """Initialize the book."""
        self.title = title.title()
        self.author = author.title()

    def describe_book(self):
        """Display a summary of the book."""
        msg = f"{self.title} is a wonderful book written by {self.author}"
        print(f"\n{msg}")

    def read_book(self):
        """Display a message that the book is being read."""
        msg = f"{self.title} is being read. It's time to read a new one."
        print(f"\n{msg}")


book = Book('crime and punishment', 'dostoevsky')
print(book.title)
print(book.author)

book.describe_book()
book.read_book()
