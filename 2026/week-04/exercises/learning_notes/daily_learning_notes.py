# Create a file called learning_notes.txt.
# Write a few notes about what you learned today in Python.
# Write a program that: reads and prints the full file
# then reads the file line by line and prints each line with a
# prefix like NOTE: before it.

from pathlib import Path

print("\n---Reading the file:")
path = Path("learning_notes.txt")
contents = path.read_text()
print(contents)

print("\nNOTE:")
lines = contents.splitlines()
for line in lines:
    print(line)
