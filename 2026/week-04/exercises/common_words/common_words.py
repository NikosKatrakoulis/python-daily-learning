# Visit Project Gutenberg and find a few texts you'd like to analyze.
# Download the text files for these works, or copy the raw text from your
# browser into a text file on your computer. You can use the count() method
# to find out how many times a word or phrase appears in a string.
# For example, the following code counts the number of times 'row'
# appers in a string:

# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# Notice that converting the string to lowercase using lower()
# catches all appearances of the word you're looking for, regardless
# of how it's formatted. Write a program that reads the files you
# found at Project Gutenberg and determines how many times the word
# 'the' appears in each text. This will be an approximation because
# it will also count words such as 'then' and 'there'. Try counting
# 'the ', with a space in the string, and see how much lower your count is.

from pathlib import Path


def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note: This is a really simple approximation and the number returned
    # will be higher than the actual count.

    path = Path(filename)
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {path.name} about {word_count} times."
        print(msg)


filename = "moby_dick.txt"
count_common_words(filename, 'the')
