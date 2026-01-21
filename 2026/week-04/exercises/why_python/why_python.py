# Create a file called why_python.txt. Write at least three sentences,
# each starting with: I like Python because...
# Write a program that: prints the entire file contents in one print
# statement then prints each line individually by looping through the lines.

from pathlib import Path

print("\n---Reading the file:")
path = Path("why_python.txt")
contents = path.read_text()
print(contents)

print("\n---Looping over the lines:")
lines = contents.splitlines()
for line in lines:
    print(line)
