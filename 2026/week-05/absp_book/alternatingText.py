#  For example, say you want a program to turn text into aLtErNaTiNg upper
# case and lowercase letters. You can copy the text you want to alternate to
# the clipboard, and then run this program, which takes this text and puts
# the alternating-case text on the clipboard.

import pyperclip

text = pyperclip.paste()  # Get the text off the clipboard.
alt_text = ''  # This string holds the alternate case
make_uppercase = False
for character in text:
    # Go through each character and add it to alt_text:
    if make_uppercase:
        alt_text += character.upper()
    else:
        alt_text += character.lower()

    # Set make_uppercase to its opposite value:
    make_uppercase = not make_uppercase

pyperclip.copy(alt_text)  # Put the result on the clipboard
print(alt_text)  # Print the result on the screen too.
