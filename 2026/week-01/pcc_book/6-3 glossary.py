# Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary. Think of five
# programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings
# as values. Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning,
# or print the word on one line and then print its meaning indented on
# a second line. Use the newline character (\n) to insert a blank
# line between each word-meaning pair in your output.

glossary = {
    'variables': 'A named container used to store data in a program.',
    'lists': 'An ordered collection of items that can be changed',
    'dictionary': 'A collection of key-value pairs used to store related data.',
    'loop': 'A way to repeat a block of code multiple times.',
    'functions': 'A reusable block of code that performs a specific task.',
}

print(f"Variables | {glossary['variables']}\n")
print(f"Lists | {glossary['lists']}\n")
print(f"Dictionary | {glossary['dictionary']}\n")
print(f"Loop | {glossary['loop']}\n")
print(f"Functions | {glossary['functions']}\n")
