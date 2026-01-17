# Create a Laptop class that contains a RAM object.
# The RAM class should have an attribute ram_size (default 8 GB) and
# a method performance_score() that prints a message based on the RAM size.
# Add a method upgrade_ram() that upgrades the RAM to 16 GB if it’s
#  not already. Create a laptop with default RAM, call
# performance_score(), upgrade the RAM, and call performance_score() again.


class Laptop:
    """A simple attempt to represent a laptop."""

    def __init__(self, brand, model, year):
        """Initialize the attributes of the laptop."""
        self.brand = brand.title()
        self.model = model.title()
        self.year = year
        self.RAM = RAM()

    def get_descriptive_name(self):
        """Display a summary of the laptop."""
        msg = f"{self.brand} {self.model} {self.year}"
        print(f"\n{msg}")


class RAM:
    """A simple attempt to model RAM for a laptop."""

    def __init__(self, ram_size=8):
        """Initialize the RAM size."""
        self.ram_size = ram_size

    def performance_score(self):
        """Print a statement estimating performance based on RAM size."""
        print(f"The laptop has the score of {self.ram_size}GB.\n")

    def upgrade_ram(self):
        """Upgrade the RAM size if possible."""
        if self.ram_size == 8:
            self.ram_size = 16
            print("Upgraded the RAM to 16GB.")
        else:
            print("The RAM is already upgraded.")


macbook = Laptop('apple', 'macbook m5 pro 16\"', 2025)
macbook.get_descriptive_name()
macbook.RAM.performance_score()

macbook.RAM.upgrade_ram()
macbook.RAM.performance_score()
