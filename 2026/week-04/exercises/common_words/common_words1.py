# Download a text file of a novel from Project Gutenberg.
# Choose a main character’s name (for example: alice, sherlock, dracula).
# Write a program that: reads the text file
# counts how many times the character’s name appears in the text
# prints the result
# Convert the text to lowercase so the count includes all variations of the
# name. Try counting the name with and without a trailing space and compare
# the results.

from pathlib import Path


def count_common_words(filename, word):
    """Count how many times word appears in the text."""

    path = Path(filename)
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {path.name} about {word_count} times."
        print(msg)


filename = "pride_and_prejudice.txt"
count_common_words(filename, 'and')
