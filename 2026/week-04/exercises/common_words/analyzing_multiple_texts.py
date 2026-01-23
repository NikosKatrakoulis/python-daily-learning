# Download two different books from Project Gutenberg and save them as
# separate text files. Write a program that: loops over a list of filenames,
# counts how many times the word 'the' appears in each file, prints a summary
# for each book.
# Try counting: 'the' and 'the ' (with a space)
# Compare the difference in results and think about why the counts
# are different.

from pathlib import Path


def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    base_path = Path(__file__).parent
    path = base_path / filename
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("Sorry, I can't find the file.")
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {path.name} about {word_count} times."
        print(msg)


filename = "common_words"

filenames = ['moby_dick.txt', 'pride_and_prejudice.txt']

print("---Counting 'the'---")
for filename in filenames:
    count_common_words(filename, 'the')

print("---Counting ' the '---")
for filename in filenames:
    count_common_words(filename, ' the ')
