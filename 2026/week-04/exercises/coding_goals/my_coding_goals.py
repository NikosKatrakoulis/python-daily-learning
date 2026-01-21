# Create a text file called coding_goals.txt.
# Write a few lines describing your goals as a programmer.
# Write a program that:
# reads the whole file and prints its contents
# then stores each line in a list and prints each line using a loop

from pathlib import Path

print("\n---Reading the file:")
path = Path("coding_goals.txt")
contents = path.read_text()
print(contents)

print("\n---Looping over the lines:")
lines = contents.splitlines()
for line in lines:
    print(line)
