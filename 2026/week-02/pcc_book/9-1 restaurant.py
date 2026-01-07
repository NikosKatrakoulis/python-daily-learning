# Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message
# indicating that the restaurant is open.

class Restaurant:
    """A class respresenting a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}!"
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is now open."""
        msg = f"{self.name} is now open. Come on in!"
        print(f"\n{msg}")


restaurant = Restaurant('Alio', 'italian food')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
