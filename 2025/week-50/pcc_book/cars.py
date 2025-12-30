# The sort() method makes it relatively easy to sort a list.
# The sort() method changes the order of the list
# permanently. The cars are now in alphabetical order, and we
# can never revert to the original order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# You can also sort this list in reverse-alphabetical order by
# passing the argument reverse=True to the sort() method.
# Again, the order of the list is permanently changed.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# To maintain the original order of a list but present it in a
# sorted order, you can use the sorted() function. The sorted()
# function lets you display your list in a particular order, but
# doesn’t affect the actual order of the list.
# The sorted() function
# can also accept a reverse=True argument if you want to
# display a list in reverse-alphabetical order.
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)


# To reverse the original order of a list, you can use the
# reverse() method. Notice that reverse() doesn’t sort backward alphabetically;
# it simply reverses the order of the list. The reverse() method changes the order of a list
# permanently, but you can revert to the original order
# anytime by applying reverse() to the same list a second
# time.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)


# You can quickly find the length of a list by using the len()
# function.Python counts the items in a list starting with one, so
# you shouldn’t run into any off-by-one errors when
# determining the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
