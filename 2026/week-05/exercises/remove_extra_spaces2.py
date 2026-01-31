# Write a program that:
# reads text from the clipboard using pyperclip.paste()
# replaces any sequence of multiple spaces with a single space
# keeps newlines (\n) unchanged
# copies the cleaned text back to the clipboard
# prints the final text

import pyperclip

text = pyperclip.paste()
result = []

prev_char = ""

for char in text:
    if char == " " and prev_char == " ":
        continue

    result.append(char)
    prev_char = char

final_text = "".join(result)
pyperclip.copy(final_text)
print(final_text)
