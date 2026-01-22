# Create two text files: foods.txt (store at least three food names)
# drinks.txt (store at least three drink names)
# Write a program that loops through a list of filenames and attempts
# to read each file. If a file exists, print its contents.
# If a file does not exist, catch the error and print a helpful message.
# Test your program by temporarily removing one of the files.

from pathlib import Path

bash_path = Path("foods&drinks")

filenames = ['foods.txt', 'drinks.txt']

for filename in filenames:
    print(f"\nReading: {filename}")

    path = bash_path / filename

    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("Sorry, I can't find the file.")
    else:
        print(contents.title())
