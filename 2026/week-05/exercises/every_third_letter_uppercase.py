# Write a program that:
# takes text from the clipboard
# converts every third character to uppercase
# leaves all other characters lowercase
# copies the modified text back to the clipboard
# prints the final result

import pyperclip

# Get text from clipboard
text = pyperclip.paste()

result_chars = []
position = 1  # Character position(starts from 1)

for character in text:
    if position % 3 == 0:
        result_chars.append(character.upper())
    else:
        result_chars.append(character.lower())

    position += 1

# Build final string
result = "".join(result_chars)

# Copy back to clipboard and print
pyperclip.copy(result)
print(result)
