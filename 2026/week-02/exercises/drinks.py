# Make a list called drink_orders and fill it with the names of various drinks
# (for example: coffee, tea, juice, water). Then make an empty list called
# finished_drinks. Loop through the list of drink orders and print a message
# for each order, such as. I prepared your coffee.As each drink is prepared,
# move it to the list of finished_drinks. After all the drinks have been
# prepared, print a message listing each drink that was prepared from
# finished_drinks.

drink_order = ['coffee', 'tea', 'juice', 'water']
finished_drinks = []

while drink_order:
    current_drink = drink_order.pop()
    print(f"I'm working on your {current_drink}.")
    finished_drinks.append(current_drink)

print("\n")
for drink in finished_drinks:
    print(f"I made a {drink}.")
