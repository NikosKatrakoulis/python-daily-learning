
# from pathlib import Path


# def count_words(path):
#     """Count the approximate number of words in a file."""
#     try:
#         contents = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         print(f"Sorry, the file {path} does not exist.")
#     else:
#         # Count the approximate number of words in the file.
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {path} has about {num_words} words.")


# path = Path("C://Dev//python-daily-learning//2026//week-02//pcc_book//alice.txt")
# count_words(path)

from pathlib import Path


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry the file {path} does not exist")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = [
    "C://Dev//python-daily-learning//2026//week-02//pcc_book//alice.txt",
    "C://Dev//python-daily-learning//2026//week-02//pcc_book//siddaharta.txt",
    "C://Dev//python-daily-learning//2026//week-02//pcc_book//moby_dick.txt",
    "C://Dev//python-daily-learning//2026//week-02//pcc_book//little_women.txt"
]
for filename in filenames:
    path = Path(filename)
    count_words(path)

# Now we can write a short loop to count the words in any
# text we want to analyze. We do this by storing the names of
# the files we want to analyze in a list, and then we call
# count_words() for each file in the list. We’ll try to count the
# words for Alice in Wonderland, Siddhartha, Moby Dick, and
# Little Women, which are all available in the public domain.
# I’ve intentionally left siddhartha.txt out of the directory
# containing word_count.py, so we can see how well our
# program handles a missing file.

# In the previous example, we informed our users that one of
# the files was unavailable. But you don’t need to report every
# exception you catch. Sometimes, you’ll want the program to
# fail silently when an exception occurs and continue on as if
# nothing happened. To make a program fail silently, you write
# a try block as usual, but you explicitly tell Python to do
# nothing in the except block. Python has a pass statement that
# tells it to do nothing in a block:

print("\n\n\n\n\n")


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = [
    "C://Dev//python-daily-learning//2026//week-02//pcc_book//alice.txt",
    "C://Dev//python-daily-learning//2026//week-02//pcc_book//siddaharta.txt",
    "C://Dev//python-daily-learning//2026//week-02//pcc_book//moby_dick.txt",
    "C://Dev//python-daily-learning//2026//week-02//pcc_book//little_women.txt"
]
for filename in filenames:
    path = Path(filename)
    count_words(path)

# The pass statement also acts as a placeholder. It’s a
# reminder that you’re choosing to do nothing at a specific
# point in your program’s execution and that you might want
# to do something there later. For example, in this program we
# might decide to write any missing filenames to a file called
# missing_files.txt. Our users wouldn’t see this file, but we’d
# be able to read the file and deal with any missing texts.
