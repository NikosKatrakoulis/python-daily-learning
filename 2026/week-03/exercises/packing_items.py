# Create a list called packing_list containing items to pack for a trip
# (e.g., "passport", "charger"). Write a function called show_packing_list()
# that prints all items. Write a function called pack_items() that prints
# each item as it is packed and moves it to a list called packed_items.
# After calling the function, print both lists to confirm everything
# moved correctly.

def show_packing_list(packing_list):
    """Print all items in the list."""
    for item in packing_list:
        print(item)


def pack_items(packing_list, packed_items):
    """Printing each item and then move it to packed_items."""
    print("\nChecking all the items:")
    while packing_list:
        current_item = packing_list.pop()
        print(current_item)
        packed_items.append(current_item)


packing_list = ["passport", "charger", "macbook", "toothbrush"]
show_packing_list(packing_list)

packed_items = []
pack_items(packing_list, packed_items)

print("\nFinal Results:")
print(packing_list)
print(packed_items)
