# An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant
# class you wrote in restaurant.py
# Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays theese flavors. Create an instance of
# IceCreamStand, and call this method.

class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display the summary of the restaurant."""
        msg = f"{self.restaurant_name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.restaurant_name} is now open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Initialize an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"-  {flavor}")


gelato_casa = IceCreamStand('gelato casa')
gelato_casa.flavors = ['nutella', 'biscuit', 'oreo']

gelato_casa.describe_restaurant()
gelato_casa.show_flavors()
