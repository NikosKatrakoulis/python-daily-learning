# Write a function called make_book() that builds a dictionary describing
# a book. The function should take in an author’s name and a book title,
# and return a dictionary with this information. Create three different
# book dictionaries using the function and print them. Add an optional
# parameter using None that allows you to store the number of pages.
# If the number of pages is provided, add it to the dictionary.
# Use the optional parameter in at least one function call.

def make_book(author, book, pages=None):
    """Build a dictionary containing information about a book."""
    book_dict = {
        'Author': author.title(),
        'Book': book.title()
    }
    if pages:
        book_dict['Pages'] = pages
    return book_dict


book = make_book("george ORWell", "1984")
print(book)
book = make_book("vladimir Nabokov", "lolita", 776)
print(book)
book = make_book("fyodor dostoievsky", "crime & punishment")
print(book)
