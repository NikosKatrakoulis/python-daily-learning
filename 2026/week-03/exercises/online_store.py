# Create a class called OnlineStore. Add two constant attributes:
# store_name, country. Add one attribute with a default value:
# orders_processed(default value: 0) Create an instance and print
# all attributes. Update the value of orders_processed directly and
# print it again. Add a method called set_orders_processed() to set
# the total number of processed orders. Add another method called
# increment_orders_processed() to increase the number of processed
# orders by a given amount. Call both methods and print the updated values.

class OnlineStore:
    """A class respresenting an online store."""

    def __init__(self, store_name, country):
        """Initialize the online store."""
        self.store_name = store_name.title()
        self.coutry = country.title()
        self.orders_processed = 0

    def describe_store(self):
        """Display a summary of the online store."""
        msg = f"{self.store_name} is the biggest online store in {self.coutry}!"
        print(f"\n{msg}")

    def set_orders_processed(self, orders_processed):
        """Allow the user to set the processed orders."""
        self.orders_processed = orders_processed

    def increment_orders_processed(self, additional_orders):
        """Allow the user to increase the processed orders."""
        self.orders_processed += additional_orders


online_store = OnlineStore('amazon', 'usa')
online_store.describe_store()

print(f"\nNumber of processed orders: {online_store.orders_processed}")
online_store.orders_processed = 50
print(f"Number of processed orders: {online_store.orders_processed}")

online_store.set_orders_processed(1500)
print(f"Number of processed orders: {online_store.orders_processed}")

online_store.increment_orders_processed(5500)
print(f"Number of processed orders: {online_store.orders_processed}")
