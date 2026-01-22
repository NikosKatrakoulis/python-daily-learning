# Write a program that prompts students to enter their name for attendance.
# Store all names in a list and write them to a file called attendance.txt,
# one name per line. Stop collecting names when the user enters 'quit'.

from pathlib import Path

path = Path("C://Users//Μακης//Documents//GitHub//python-daily-learning//2026//week-04//exercises//attendance//attendance.txt")

prompt = "\nWhat is your name?"
prompt += "\nEnter 'quit' to stop if you are the last one."

names = []

while True:
    name = input(prompt)
    if name == 'quit':
        break

    print(
        f"\nThank you {name.title()} for telling me your name. I needed it for attendance.")
    names.append(name)

name_string = ''
for name in names:
    name_string += f"{name.title()}\n"

path.write_text(name_string)
