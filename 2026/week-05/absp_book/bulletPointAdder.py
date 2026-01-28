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

# When this program is run, it replaces the text on the clipboard with text
# that has stars at the start of each line. Now the program is complete, and you
# can try running it with text copied to the clipboard.
# Even if you don’t need to automate this specific task, you might want to
# automate some other kind of text manipulation, such as removing trailing
# spaces from the end of lines or converting text to uppercase or lowercase.
# Whatever your needs, you can use the clipboard for input and output.
