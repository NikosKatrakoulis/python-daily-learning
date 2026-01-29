# Write a program that:
# reads text from the clipboard using pyperclip.paste()
# converts each lowercase letter to uppercase and each uppercase letter
# to lowercase leaves non-letter characters unchanged
# copies the transformed text back to the clipboard
# prints the result to the screen

import pyperclip

text = pyperclip.paste()
alt_text = []
make_uppercase = False

for character in text:
    if character.isalpha():
        if make_uppercase:
            alt_text.append(character.upper())
        else:
            alt_text.append(character.lower())
            make_uppercase = not make_uppercase
    else:
        alt_text.append(character)

result = "".join(alt_text)
pyperclip.copy(result)
print(result)
