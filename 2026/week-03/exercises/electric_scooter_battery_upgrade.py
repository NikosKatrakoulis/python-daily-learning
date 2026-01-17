# Create a Scooter class that contains a Battery object.
# The battery should have an attribute battery_size (default 30)
# and a method get_range() that prints range based on the battery size.
# Add a method upgrade_battery() that upgrades battery_size to 50
# if it’s not already. Create a scooter with default battery,
# call get_range(), upgrade the battery, and call get_range()
# again to show increased range.

class Scooter:
    """A single attempt to represent a scooter."""

    def __init__(self):
        """Initialize the atttributes of the scooter."""
        self.battery_size = Battery()


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=30):
        """Initialize the attributes of the battery."""
        self.battery_size = battery_size

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 30:
            range = 20
        elif self.battery_size == 50:
            range = 35
        print(f"\nThus scooter can go about {range} kilometers.")

    def uprgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 30:
            self.battery_size = 50
            print(f"\nUpgraded battery to {self.battery_size}-kWh.")
        else:
            print("The battery is already upgraded.")


scooter = Scooter()
scooter.battery_size.get_range()

scooter.battery_size.uprgrade_battery()
scooter.battery_size.get_range()
