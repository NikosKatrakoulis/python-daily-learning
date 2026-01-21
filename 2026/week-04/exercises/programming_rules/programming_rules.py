# Create a file called programming_rules.txt.
# Write at least four rules you want to follow while learning programming.
# Write a program that: reads the file and prints the entire contents
# then loops through the lines and prints them one by one

from pathlib import Path

print("\n---Reading the file:")
path = Path("programming_rules.txt")
contents = path.read_text()
print(contents)

print("\n---Looping over the line:")
lines = contents.splitlines()
for line in lines:
    print(line)
