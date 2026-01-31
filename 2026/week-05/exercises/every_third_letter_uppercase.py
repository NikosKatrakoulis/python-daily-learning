# Write a program that:
# takes text from the clipboard
# converts every third character to uppercase
# leaves all other characters lowercase
# copies the modified text back to the clipboard
# prints the final result

import pyperclip

text = pyperclip.paste()
changed_text = []

position = 1

for character in text:
    if character.isalpha():
        if position % 3 == 0:
            changed_text.append(character.upper())
        else:
            changed_text.append(character.lower())
        position += 1
    else:
        changed_text.append(character)

result = "".join(changed_text)
pyperclip.copy(result)
print(result)
