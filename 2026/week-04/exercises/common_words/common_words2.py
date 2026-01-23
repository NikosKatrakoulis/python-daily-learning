# Choose a text file from Project Gutenberg.
# Write a program that counts how many times two different common words appear in the text (for example: and and but).

# Your program should:

# read the file safely using try-except

# convert the text to lowercase

# print how many times each word appears

# Compare which word appears more frequently in the text.

from pathlib import Path


def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    path = Path(filename)
    try:
        contents = path.read_text(encoding="utf=8")
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in the {path.name} about {word_count} times."
        print(msg)


filename = "pride_and_prejudice.txt"

count_common_words(filename, 'and')
count_common_words(filename, 'but')
