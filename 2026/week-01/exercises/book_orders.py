# Make a list called book_orders and an empty list called finished_books.
# Process each book and move it to the finished list.

book_orders = ['LOTR 1', 'LOTR 2', 'LOTR 3', 'Harry Potter 1', 'Harry Potter 2',
               'Harry Potter 3', 'Harry Potter 4', 'Harry Potter 5', 'Harry Potter 6', 'Harry Potter 7',]

finished_books = []

while book_orders:
    current_book = book_orders.pop()
    print(f"I processed the book: {current_book}.")
    finished_books.append(current_book)

print(f"\nFinished Orders:")
for book in finished_books:
    print(book)
