# Write a program that:
# reads text from the clipboard
# converts vowels (a, e, i, o, u) to uppercase
# converts all other letters to lowercase
# keeps spaces and punctuation unchanged
# copies the result back to the clipboard
# prints the final text

import pyperclip

# Read text from the clipboard
text = pyperclip.paste()

VOWELS = "aieou"
result = ""

for char in text:
    if char.isalpha():
        if char.lower() in VOWELS:
            result += char.upper()
        else:
            result += char.lower()
    else:
        # Keep spaces,punctuation and numbers as they are
        result += char
# Copy result back to the clipboard
pyperclip.copy(result)

# Print final text
print(result)
