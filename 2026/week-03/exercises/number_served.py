# Start with your program from restaurant.py. Add an attribute called
# number_served with a default value of 0. Create an instance called
# restaurant from this class. Print the number of customers the restaurant
# has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number
# and print the value again. Add a method called increment_number_served()
# that lets you increment the number of customers who've been served.
# Call this method with any number you like that could represent how many
# customers were served in, say, a day of business.

class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Display the summary of the restaurant."""
        print(f"\n{self.restaurant_name} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"{self.restaurant_name} is now open. Come on in!")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


restaurant = Restaurant('Alio', 'pizza')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 500
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1000)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(250)
print(f"Number served: {restaurant.number_served}")
