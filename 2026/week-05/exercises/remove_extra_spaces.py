# You have the string: "Python is awesome".
# Use split() (with no argument) and then " ".join(...) to produce:
# "Python is awesome" (single spaces only). Print the result.

string_to_list = "Python is awesome".split()
print(string_to_list)
list_to_string = ' '.join(string_to_list[:])
print(list_to_string)
