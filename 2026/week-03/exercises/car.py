# Make a class called Car.
# The __init__() method should store two attributes: brand and model.
# Add a method called describe_car() that prints the car’s brand and model.
# Add a method called start_car() that prints a message indicating the car
# has started. Create an instance of Car.
# Print the attributes individually, and then call both methods.

class Car:
    """A class representing a car."""

    def __init__(self, brand, model):
        """Initialize the car."""
        self.brand = brand.title()
        self.model = model.title()

    def describe_car(self):
        """Display a summary of the car."""
        msg = f"{self.brand} has my favorite car which the model is {self.model}."
        print(f"\n{msg}")

    def start_car(self):
        """Display that the car has started."""
        msg = f"Nikos has started to go at his girlfriend with his new {self.brand}."
        print(f"\n{msg}")


car = Car('ferrari', 'portofino')
print(car.brand)
print(car.model)

car.describe_car()
car.start_car()
