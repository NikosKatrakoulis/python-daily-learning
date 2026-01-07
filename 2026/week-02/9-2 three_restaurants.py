# Three Restaurants: Start with your class from Exercise 9-1. Create
# three different instances from the class, and call describe_restaurant() for
# each instance.

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


restaurant = Restaurant('alio', 'pizza')
restaurant.describe_restaurant()


restaurant = Restaurant('anemologio', 'souvlaki')
restaurant.describe_restaurant()


restaurant = Restaurant('selim bey', 'lahmatzoun')
restaurant.describe_restaurant()
