# Let’s create a module containing just the Car class.
# The import statement ❶ tells Python to open the car
# module and import the class Car. Now we can use the Car
# class as if it were defined in this file. The output is the same
# as we saw earlier.
# Importing classes is an effective way to program. Picture
# how long this program file would be if the entire Car class
# were included. When you instead move the class to a
# module and import the module, you still get all the same
# functionality, but you keep your main program file clean and
# easy to read. You also store most of the logic in separate
# f
# iles; once your classes work as you want them to, you can
# leave those files alone and focus on the higher-level logic of
# your main program.


"""A class that can by used to represent a car."""


class Car:
    """A simple attempt to respresent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a astatement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer
        back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
