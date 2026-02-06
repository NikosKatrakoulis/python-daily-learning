# Write a program that:
# asks the user for a text
# uses a regular expression to check if the word "python" appears in the text
# prints a message indicating whether it was found or not
# Goal: re.search(), basic pattern

import re

text = input("Enter me a text:")

pattern = re.compile(r"python", re.IGNORECASE)

match = pattern.search(text)

if match:
    print("The word 'python' was found in text.")
else:
    print("The word 'python' was not found in text.")
