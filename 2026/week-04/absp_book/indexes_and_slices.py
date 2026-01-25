# Strings use indexes and slices the same way lists do. You can think of the
# string 'Hello, world!' as a list and each character in the string as an item
# with a corresponding index and negative index.

greeting = 'Hello, world!'
print(greeting[0])

print(greeting[4])

print(greeting[-1])

print(greeting[0:5])

print(greeting[:5])

print(greeting[7:-1])

print(greeting[7:])


# If you specify an index, you’ll get the character at that position in the
# string. If you specify a range from one index to another, the starting index
# is included and the ending index is not. That’s why, if greeting is 'Hello,
# world!', then greeting[0:5] evaluates to 'Hello'. The substring you get from
# greeting[0:5] will include everything from greeting[0] to greeting[4], leaving
# out the comma at index 5 and the space at index 6. This is similar to how
# range(5) will cause a for loop to iterate up to, but not including, 5.
