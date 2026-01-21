from pathlib import Path

path = Path(
    "pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# When Python reads from a text file, it interprets all
# text in the file as a string. If you read in a number and
# want to work with that value in a numerical context,
# you’ll have to convert it to an integer using the int()
# function or a float using the float() function.


path = Path(
    "pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:55]}")
print(len(pi_string))


# Let’s use the program we just
# wrote to find out if someone’s birthday appears anywhere in
# the first million digits of pi. We can do this by expressing
# each birthday as a string of digits and seeing if that string
# appears anywhere in pi_string:

path = Path(
    "pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits on pi!")
else:
    print("Your birthday does not appear in the first million digits on pi.")
