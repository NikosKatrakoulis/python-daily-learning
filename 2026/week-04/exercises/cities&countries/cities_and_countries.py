# Create two files: cities.txt (store at least three city names)
# countries.txt (store at least three country names)
# Write a program that attempts to read both files and print their
# contents to the screen. Wrap your file-reading code in a try-except
# block to catch FileNotFoundError. If a file is missing, print a
# friendly message saying the file could not be found.
# Move or rename one of the files to make sure the except block
# runs correctly.

from pathlib import Path

bash_path = Path("cities&countries")

filenames = ['cities.txt', 'countries.txt']

for filename in filenames:
    print(f"\nReading: {filename}")

    path = bash_path / filename

    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("Sorry, I can't find the file.")
    else:
        print(contents.title())
