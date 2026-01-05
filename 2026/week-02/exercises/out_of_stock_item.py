# Using a list of store_orders, make sure the item "chips" appears at
# least three times. Print a message that the store has run out of chips,
# and then use a while loop to remove all occurrences of "chips" from
# store_orders. Then process the remaining orders normally (no chips
# should be processed).

store_orders = ["chips", "bread", "chips", "eggs", "chips"]

print("Sorry, we are out of chips!")

while "chips" in store_orders:
    store_orders.remove("chips")

print("---Remaining Orders---")
for order in store_orders:
    print(f" -{order}")
