# Create two files: books.txt (store at least three book titles)
# movies.txt (store at least three movie titles)
# Write a program that tries to read and display the contents of both files.
# Use a try-except block to handle missing files gracefully.
# Move one of the files to another folder to confirm that your error-handling
# code works correctly.

from pathlib import Path

bash_path = Path(
    "C://Users//Μακης//Documents//GitHub//python-daily-learning//2026//week-04//exercises//books&movies")

filenames = ['books.txt', 'movies.txt']

for filename in filenames:
    print(f"\n---Reading file: {filename}")

    path = bash_path / filename

    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("Sorry, I can't find the file.")
    else:
        print(contents.title())
