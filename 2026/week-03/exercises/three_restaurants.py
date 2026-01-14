# Start with your class from file restaurant.py . Create three different
# instances from the class, and call describe_restaurant() for each instance.

class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.restaurant_name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.restaurant_name} is open. Come on in!"
        print(f"\n{msg}")


alio = Restaurant('Alio', 'pizza')
alio.describe_restaurant()

selim_bey = Restaurant('selim bey', 'lahmacun')
selim_bey.describe_restaurant()

el_catrin = Restaurant('el catrin', 'tacos')
el_catrin.describe_restaurant()
