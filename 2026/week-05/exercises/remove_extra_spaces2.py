# Write a program that:
# reads text from the clipboard using pyperclip.paste()
# replaces any sequence of multiple spaces with a single space
# keeps newlines (\n) unchanged
# copies the cleaned text back to the clipboard
# prints the final text

import pyperclip

text = pyperclip.paste()
reverse_text = []
make_uppercase = False

for character in text:
    if character.isalpha():
        if make_uppercase:
            reverse_text.append(character.upper())
        else:
            reverse_text.append(character.lower())
        make_uppercase = not make_uppercase
    else:
        reverse_text.append(character)

result = "".join(reverse_text)
pyperclip.copy(result)
print(result)
