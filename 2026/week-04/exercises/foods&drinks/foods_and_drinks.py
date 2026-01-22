# Create two text files: foods.txt (store at least three food names)
# drinks.txt (store at least three drink names)
# Write a program that loops through a list of filenames and attempts
# to read each file. If a file exists, print its contents.
# If a file does not exist, catch the error and print a helpful message.
# Test your program by temporarily removing one of the files.

from pathlib import Path

bash_path = Path(
    "C://Users//Μακης//Documents//GitHub//python-daily-learning//2026//week-04//exercises//foods&drinks")

filenames = ['foods.txt', 'drinks.txt']

for filename in filenames:
    print(f"\nReading: {filename}")

    path = bash_path / filename

    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("Sorry, Icant find the file.")
    else:
        print(contents.title())
