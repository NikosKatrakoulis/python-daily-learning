# You can place an r before the beginning quotation mark of a string literal
# to make it a raw string literal. A raw string makes it easier to enter string
# values that have backslashes by ignoring all escape characters. For example,
# enter the following into the interactive shell:

print(r'The file is in C:\Users\Alice\Desktop')

# Because this is a raw string, Python considers the backslash to be part
# of the string and not the start of an escape character:

# Without a raw string
print('Hello...\n\n...world!')

# With a raw string
print(r'Hello...\n\n...world!')
