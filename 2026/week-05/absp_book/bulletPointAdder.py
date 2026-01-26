# When editing a Wikipedia article, you can create a bulleted list by
# putting each list item on its own line and placing a star in front of it.
# But say you have a really large list that you want to add bullet points
# to. You could type those stars at the beginning of each line, one by one.
# Or you could automate this task with a short Python script.
# The bulletPointAdder.py script will get the text from the clipboard, add
# a star and space to the beginning of each line, and then paste this new
# text to the clipboard.


import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):  # Loop through all indexes in the "lines" list.
    # Add a star to each string in the "lines" list.
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
print(text)
