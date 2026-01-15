# A coffee shop is a specific kind of restaurant.
# Create a class called CoffeeShop that inherits from a Restaurant class.
# Add an attribute called drinks that stores a list of available coffee
# drinks. Write a method called show_drinks() that displays all the drinks.
# Create an instance of CoffeeShop, add at least three drinks to the list,
# and call describe_restaurant() and show_drinks().

class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
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
        print(msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customer that have been served."""
        self.number_served = number_served

    def icrement_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class CoffeeShop(Restaurant):
    """A class representing a coffee shop."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Initialize the coffee shop."""
        super().__init__(restaurant_name, cuisine_type)
        self.drinks = []

    def show_drinks(self):
        """Display the drinks available."""
        print("\nWe have the following drinks available:")
        for drink in self.drinks:
            print(f"-  {drink}")


nut_cap = CoffeeShop('nut cap')
nut_cap.drinks = ['cappucino', 'orange juice', 'greek coffee']

nut_cap.describe_restaurant()
nut_cap.show_drinks()
