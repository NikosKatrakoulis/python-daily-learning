# Ask the user to enter items in one line separated by commas,
# for example: "milk, bread, eggs".
# Use split(',') to turn it into a list, clean up extra spaces
# around each item, and then print the items joined by " | " using join().

items_input = input("Enter items separated by commas:")

items = items_input.split(',')

clean_items = []
for item in items:
    clean_items.append(item.strip())

result = ' | '.join(clean_items)
print(result)
