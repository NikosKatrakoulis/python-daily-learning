# Glossary 2: Now that you know how to loop through a dictionary,
# clean up the code from Exercise 6-3 (page 99) by replacing your
# series of print() calls with a loop that runs through the dictionary’s
# keys and values. When you’re sure that your loop works, add five
# more Python terms to your glossary. When you run your program again,
# these new words and meanings should automatically be included in the
# output.

glossary = {
    'variables': 'A named container used to store data in a program.',
    'lists': 'An ordered collection of items that can be changed',
    'dictionary': 'A collection of key-value pairs used to store related data.',
    'loop': 'A way to repeat a block of code multiple times.',
    'functions': 'A reusable block of code that performs a specific task.',

    # New terms
    'tuple': 'An ordered collection of items than cannot be changed.',
    'boolean': 'A data type that can be either True or False.',
    'index': 'A position number used to access an item in a sequence.',
    'slice': 'A portion of a list or string.',
    'key': 'A unique indetifier used to access a value in a dictionary.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}:")
    print(f"{meaning}\n")

# or


for word in sorted(glossary):
    print(f"{word.title()}:")
    print(f"{glossary[word]}\n")
