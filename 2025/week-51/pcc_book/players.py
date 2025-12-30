# Slicing a List. To output the first three elements in a list, you
# would request indices 0 through 3, which would return
# elements 0, 1, and 2.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])


print(players[1:4])

# If you omit the first index in a slice, Python automatically
# starts your slice at the beginning of the list.
print(players[:3])

# A similar syntax works if you want a slice that includes the
# end of a list. For example, if you want all items from the
# third item through the last item, you can start with index 2
# and omit the second index.
print(players[2:])

print(players[-2:])

# You can use a slice in a for loop if you want to loop through
# a subset of the elements in a list. In the next example, we
# loop through the first three players and print their names as
# part of a simple roster.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
