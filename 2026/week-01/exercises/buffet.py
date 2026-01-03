# Buffet: A buffet-style restaurant offers only five basic foods.
# Think of five simple foods and store them in a tuple. Use a for
# loop to print each food the restaurant offers. Try to modify one
# of the items and make sure that Python rejects the change. The
# restaurant changes its menu, replacing two of the items with
# different foods. Add a line that rewrites the tuple, and then
# use a for loop to print each of the items on the revised menu.

foods = ('pastitsio', 'mousakas', 'spaghetti ala creme',
         'lentiles soup', 'cheese pie')

print("\n===Main Menu===")
for food in foods:
    print(food.title())

# Intentional error
# foods[0] = 'ratatouille'
# print(foods[0])

foods = ('tacos with chicken', 'ceasar salad', 'double cheese burger',
         'carbonara', 'pulled pork with fries')
print("\n===Revised Menu===")
for food in foods:
    print(food.title())
