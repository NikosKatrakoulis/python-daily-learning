# Create a text file called favorite_concepts.txt.
# Write at least three lines about your favorite programming concepts.
# Start each line with the phrase: One thing I like about programming is...
# Write a program that:
# reads and prints the entire file at once
# then reads the file line by line and prints each line separately

from pathlib import Path

print("\n---Reading the file:")
path = Path("favorite_concepts.txt")
contents = path.read_text()
print(contents)

print("\n---Looping over the file:")
lines = contents.splitlines()
for line in lines:
    print(line)
