# Write a regex that matches:
# either "Mr. Smith"
# or "Smith"
# and write a program that tests it on various strings.
# Goal: ? and optional groups

import re

pattern = re.compile(r"^(?:Mr\.\s)?[A-Za-z]+$")

tests = ["Mr.Smith", "Smith", "Mr Smith", "Mr.Smith!", "Dr.Smith"]

for text in tests:
    if pattern.search(text):
        print(f"OK: {text}")
    else:
        print(f"NO: {text}")
