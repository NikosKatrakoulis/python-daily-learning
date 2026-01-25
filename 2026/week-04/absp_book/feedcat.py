# While you can use the \n escape character to insert a newline into a
# string, it’s often easier to use multiline strings. A multiline string
# in Python begins and ends with either three single quotes or three double
# quotes. Any quotes, tabs, or newlines in between the “triple quotes” are
# considered part of the string. Python’s indentation rules for blocks don’t
# apply to lines inside a multiline string.

print('''Dear Alice,

Can you feed Eve's cat this weekend?
      
Sincerely,
Bob''')

# Notice that the single quote character in Eve's doesn’t need to be
# escaped. Escaping single and double quotes is optional in multiline strings
