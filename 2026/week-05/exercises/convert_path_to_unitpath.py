# You have a Windows path string: "C:\\Users\\Nikos\\Documents\\file.txt".
# Use split('\\') to separate the parts, then use "/".join(...) to
# rebuild it as: "C:/Users/Nikos/Documents/file.txt".

path = "C:\\Users\\Nikos\\Documents\\file.txt".split('\\')

result = '/'.join(path)

print(result)
