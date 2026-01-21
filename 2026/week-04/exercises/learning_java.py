# You can use the replace() method to replace any word in a string with
# a different word. Here's a quick example showing how to replace
# 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'

from pathlib import Path

path = Path("learning_notes.txt")
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'Java')
    print(line)
