# More Guests: You just found a bigger dinner table,
# so now more space is available. Think of three more guests
# to invite to dinner. Start with your program from
# Exercise 3-4 or 3-5. Add a print() call to the end of your
# program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.


guests = ['sofia', 'meletis', 'dimitris']
print("Good news! I found a bigger dinner table!")

guests.insert(0, 'thakis')
guests.insert(2, 'giorgos')
guests.append('stathis')

for guest in guests:
    print(
        f"Hello {guest.title()}, I'd like to invite you to dinner on Sunday evening.")
