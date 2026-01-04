# A bakery has run out of chocolate donuts.
# Remove all "chocolate" items from the orders list before processing.

donut_orders = ['chocolate', 'vanilla', 'chocolate', 'strawberry', 'chocolate']

print("Sorry, we are out of chocolate donuts.")

while 'chocolate' in donut_orders:
    donut_orders.remove('chocolate')

print("Remaining Orders:")

for donut in donut_orders:
    print(f" -{donut.title()}")
