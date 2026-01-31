# Write a program that:
# reads text from the clipboard
# converts vowels (a, e, i, o, u) to uppercase
# converts all other letters to lowercase
# keeps spaces and punctuation unchanged
# copies the result back to the clipboard
# prints the final text

import pyperclip

text = pyperclip.paste()
result_text = []

VOWELS = "aeiou"

for character in text:
    if character.isalpha():
        if character in VOWELS:
            result_text.append(character.upper())
        else:
            result_text.append(character.lower())
    else:
        result_text.append(character)

result = "".join(result_text)
pyperclip.copy(result)
print(result)
