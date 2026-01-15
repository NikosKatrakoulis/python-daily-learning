# An animal shelter can have a special type: a dog shelter. Create a class
# called Shelter with attributes like shelter_name and city, and a method
# called describe_shelter(). Then create a class called DogShelter that
# inherits from Shelter. Add an attribute called dogs that stores a
# list of dog names currently in the shelter. Write a method called
# show_dogs() to display all dog names. Create an instance of DogShelter,
# add at least three dog names, and call both methods.

class Shelter:
    """A class representing a shelter."""

    def __init__(self, shelter_name, city):
        """Initialize the shelter."""
        self.shelter_name = shelter_name.title()
        self.city = city.title()

    def describe_shelter(self):
        """Display the summary of the shelter."""
        msg = f"{self.shelter_name} is a shelter in {self.city}."
        print(f"\n{msg}")


class DogShelter(Shelter):
    """A class representing a dog shelter."""

    def __init__(self, shelter_name, city):
        """Initialize the dog shelter."""
        super().__init__(shelter_name, city)
        self.dogs = []

    def show_dogs(self):
        """Display the dog names."""
        print("\nWe have the following dogs in your shelter:")
        for dog in self.dogs:
            print(f"- {dog.title()}")


kritikos = DogShelter('kritikos', 'megara')
kritikos.dogs = ['roby', 'frida', 'larry', 'rex']

kritikos.describe_shelter()
kritikos.show_dogs()
