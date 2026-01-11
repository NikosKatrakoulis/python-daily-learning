# One common issue when working with files is handling
# missing files. The file you’re looking for might be in a
# different location, the filename might be misspelled, or the
# f
# ile might not exist at all. You can handle all of these
# situations with a try-except block.

"""
from pathlib import Path

path = Path('alice.txt')
contents = path.read_text(encoding='utf-8')

"""

# Note that we’re using read_text() in a slightly different way
# here than what you saw earlier. The encoding argument is
# needed when your system’s default encoding doesn’t match
# the encoding of the file that’s being read. This is most likely
# to happen when reading from a file that wasn’t created on
# your system.
# Python can’t read from a missing file, so it raises an
# exception.

# In this example, the code in the try block produces a
# FileNotFoundError, so we write an except block that matches
# that error. Python then runs the code in that block when
# the file can’t be found, and the result is a friendly error
# message instead of a traceback:
# Sorry, the file alice.txt does not exist.


from pathlib import Path

path = Path("C://Dev//python-daily-learning//2026//week-02//pcc_book//alice.txt")
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

# Let’s pull in the text of Alice in Wonderland and try to
# count the number of words in the text. To do this, we’ll use
# the string method split(), which by default splits a string
# wherever it finds any whitespace:


path = Path("C://Dev//python-daily-learning//2026//week-02//pcc_book//alice.txt")
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
