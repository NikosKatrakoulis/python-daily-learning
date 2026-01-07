# Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class you
# wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version
# of the class will work; just pick the one you like better. Add an attribute
# called flavors that stores a list of ice cream flavors. Write a method that
# displays these flavors. Create an instance of IceCreamStand, and call this
# method.

class Restaurant:
    """A class respresenting a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}!"
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is now open."""
        msg = f"{self.name} is now open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


ice_cream = IceCreamStand('Ice Cream Paradise')
ice_cream.flavors = ['nutella', 'cookies', 'biscuit']

ice_cream.describe_restaurant()
ice_cream.show_flavors()
