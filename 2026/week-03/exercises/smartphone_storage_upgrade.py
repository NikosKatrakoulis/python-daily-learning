# Use a Smartphone class that contains a Storage object (composition).
# The Storage class should have an attribute like capacity (default 64 GB)
# and a method get_available_space() that prints a message based on the
# capacity.Add a method upgrade_storage() to Storage that upgrades
# the capacity to 128 GB if it isn’t already. Create a smartphone
# with default storage, call get_available_space(), upgrade the
# storage, and call get_available_space() again to show the change.


class Smartphone:
    """A simple attempt to represent a phone."""

    def __init__(self, brand, model, year):
        """Initialize the attributes of the smartphone."""
        self.brand = brand
        self.model = model
        self.year = year
        self.storage = Storage()

    def get_descriptive_name(self):
        """Display a summary of the phone."""
        desc = f"{self.brand} {self.model} {self.year}"
        print(desc.title())


class Storage:
    """A simple attempt to model storage space to a smartphone."""

    def __init__(self, capacity=64):
        """Initialize the Storage's attributes."""
        self.capacity = capacity

    def get_available_space(self):
        """Print a statement about the capacity this storage provides."""
        print(f"This phone has {self.capacity} GB of storage.")

    def upgrade_storage(self):
        """Upgrade the capacity if possible."""
        if self.capacity == 64:
            self.capacity = 128
            print("Upgraded the storage to 128GB.")
        else:
            print("The phone's storage is already upgraded.")


iphone = Smartphone('apple', 'iphone 17 pro max', 2025)
iphone.get_descriptive_name()
iphone.storage.get_available_space()

print("\n")
iphone.storage.upgrade_storage()
iphone.storage.get_available_space()
