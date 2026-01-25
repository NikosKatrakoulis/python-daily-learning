# Python has a removesuffix() method that works exactly like removeprefix().
# Assign the value 'python_notes.txt' to a variable called filename.
# Then use the removesuffix() method to display the filename without the
# file extension, like some file browsers do.

filename = 'python_notes.txt'
simple_filename = filename.removesuffix('.txt')

print(simple_filename)

url = 'https://www.facebook.com'
simple_url = url.removeprefix('https://www.')
print(simple_url)
