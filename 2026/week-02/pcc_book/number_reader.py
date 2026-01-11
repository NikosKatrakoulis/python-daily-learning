# Now we’ll write a separate program that uses json.loads()
# to read the list back into memory:

from pathlib import Path
import json

path = Path(
    "C://Dev//python-daily-learning//2026//week-02//pcc_book//numbers.json")
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)

# We make sure to read from the same file we wrote to.
# Since the data file is just a text file with specific formatting,
# we can read it with the read_text() method. We then pass
# the contents of the file to json.loads(). This function takes
# in a JSON-formatted string and returns a Python object (in
# this case, a list), which we assign to numbers. Finally, we print
# the recovered list of numbers and see that it’s the same list
# created in number_writer.py:
# [2, 3, 5, 7, 11, 13]
# This is a simple way to share data between two programs.
