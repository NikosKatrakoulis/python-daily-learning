# Create a function that builds a dictionary describing a book.
# The function should take in a book title and the author’s name
# and return a dictionary. Write a while loop that allows users to
# enter a book title and author. Call the function with the user’s
# input and print the dictionary that’s created.
# Be sure to include a quit option in the loop.

def make_book(author, book, pages=None):
    """Build a dictionary containing information about a book."""
    book_dict = {
        'Author': author.title(),
        'Book': book.title()
    }
    if pages:
        book_dict['Pages'] = pages
    return book_dict


# Prepare the prompts.
book_prompt = "\nWhat book are you thinking of?"
author_prompt = "Who is the author?"

# Let user know how to quit.
print("Enter 'quit' to stop.")

while True:

    book = input(book_prompt)
    if book == 'quit':
        break
    author = input(author_prompt)
    if author == 'quit':
        break

    book = make_book(author, book)
    print(book)

print("\nThanks for responding!")
