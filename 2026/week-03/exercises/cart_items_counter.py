# Create a class called ShoppingCart. Add attributes like owner_name
# and cart_id. Add an attribute called items_added with a default value of 0.
# Write a method called add_item() that increments items_added by 1.
# Write a method called clear_cart() that resets items_added to 0.
# Create an instance of ShoppingCart, call add_item() multiple times,
# print the counter, then call clear_cart() and print again.

class ShoppingCart:
    """A class representing a shopping cart."""

    def __init__(self, owner_name, cart_id):
        """Initialize the shopping cart."""
        self.owner_name = owner_name.title()
        self.cart_id = cart_id
        self.items_added = 0

    def describe_shopping_cart(self):
        """Display a summary of the shopping cart."""
        print(f"\nOwner: {self.owner_name}")
        print(f"Cart ID: {self.cart_id}")

    def greet_owner(self):
        """Display the personalized greeting."""
        print(f"\nHello {self.owner_name}, this your shopping cart app.")

    def add_item(self):
        """Adding the number of the items."""
        self.items_added += 1

    def clear_cart(self):
        """Resetting the items to 0."""
        self.items_added = 0


cart = ShoppingCart('Nikos Katrakoulis', 5460_9877_1244_675)
cart.describe_shopping_cart()
cart.greet_owner()

print("\nAdding 13 items...")
cart.add_item()
cart.add_item()
cart.add_item()
cart.add_item()
cart.add_item()
cart.add_item()
cart.add_item()
cart.add_item()
cart.add_item()
cart.add_item()
cart.add_item()
cart.add_item()
cart.add_item()
print(f"    Number of Items: {cart.items_added}")

print("\nResetting the items on the cart.")
cart.clear_cart()
print(f"    Number of items: {cart.items_added}")
