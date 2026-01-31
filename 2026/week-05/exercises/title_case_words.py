# Write a program that:
# reads text from the clipboard
# converts the text so that the first letter of each word is uppercase and
# the remaining letters are lowercase
# keeps punctuation unchanged as much as possible
# copies the result back to the clipboard
# prints the final text

import pyperclip

text = pyperclip.paste()
result = []
new_word = True  # True means that the next letter starts a new word

for char in text:
    if char.isalpha():
        if new_word:
            result.append(char.upper())
            new_word = False
        else:
            result.append(char.lower())

    else:
        # keep punctuation, numbers, spaces and newlines unchanged
        result.append(char)

    if char.isspace():
        # If we hit a separator or next letter starts a new word
        new_word = True

final_text = "".join(result)
pyperclip.copy(final_text)
print(final_text)
