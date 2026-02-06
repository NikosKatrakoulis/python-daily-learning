# Write a program that:
# takes a text
# finds all numbers contained in the text
# prints them in a list
# Goal: re.findall()

import re

text = input("Enter a text:")

pattern = re.compile(r"\d+")
numbers = pattern.findall(text)

print("We found the following numbers:", numbers)
