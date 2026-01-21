# Write a program that asks users a survey question such as
# “What is your favorite hobby?”
# Store each response in a list and write all responses to a file
# called survey_results.txt, with one response per line.
# Allow users to stop the program by entering 'quit'.

from pathlib import Path

path = Path("survey_responses.txt")

prompt = "\nWhat is your favorite hobby?"
prompt += "\nEnter 'quit' if you are the last person."

favorite_hobby = []
while True:
    hobby = input(prompt)
    if hobby == 'quit':
        break

    print("\nThanks for the response!")
    favorite_hobby.append(hobby)

hobby_string = ''
for hobby in favorite_hobby:
    hobby_string += f"{hobby}\n"

path.write_text(hobby_string)
