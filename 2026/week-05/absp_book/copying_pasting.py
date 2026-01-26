# The pyperclip module has copy() and paste() functions that can send text
# to and receive text from your computer’s clipboard. Sending the output of
# your program to the clipboard will make it easy to paste it into an email,
# a word processor, or some other software.

import pyperclip

msg = pyperclip.copy('Hello,world!')
msg = pyperclip.paste()
print(msg)


# The clipboard is an excellent way to enter and receive large amounts
# of text without having to type it when prompted by an input() call.
