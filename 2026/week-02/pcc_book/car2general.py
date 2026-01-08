# Let’s write a class representing a car. Our class will
# store information about the kind of car we’re working with,
# and it will have a method that summarizes this information:

class Car:
    """A simple attempt to respresent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())


# When an instance is created, attributes can be defined
# without being passed in as parameters. These attributes can
# be defined in the __init__() method, where they are
# assigned a default value.
# Let’s add an attribute called odometer_reading that always
# starts with a value of 0. We’ll also add a method
# read_odometer() that helps us read each car’s odometer.

class Car:
    """A simple attempt to respresent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's milesage."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# You can change an attribute’s value in three ways: you can
# change the value directly through an instance, set the value
# through a method, or increment the value (add a certain
# amount to it) through a method. Let’s look at each of these
# approaches.

# The simplest way to modify the value of an attribute is to
# access the attribute directly through an instance.
# We use dot notation to access the car’s odometer_reading
# attribute, and set its value directly. This line tells Python to
# take the instance my_new_car, find the attribute
# odometer_reading associated with it, and set the value of that
# attribute to 23:

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# It can be helpful to have methods that update certain
# attributes for you. Instead of accessing the attribute
# directly, you pass the new value to a method that handles
# the updating internally.
# Here’s an example showing a method called
# update_odometer():


class Car:
    """A simple attempt to respresent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's milesage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()


# We can extend the method update_odometer() to do
# additional work every time the odometer reading is
# modified. Let’s add a little logic to make sure no one tries to
# roll back the odometer reading:


class Car:
    """A simple attempt to respresent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's milesage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
           Reject the change if it attemps to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()


# Sometimes you’ll want to increment an attribute’s value by
# a certain amount, rather than set an entirely new value. Say
# we buy a used car and put 100 miles on it between the time
# we buy it and the time we register it. Here’s a method that
# allows us to pass this incremental amount and add that
# value to the odometer reading:


class Car:
    """A simple attempt to respresent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's milesage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
           Reject the change if it attemps to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()

# The new method increment_odometer() takes in a number of
# miles, and adds this value to self.odometer_reading. First, we
# create a used car, my_used_car ❶. We set its odometer to
# 23,500 by calling update_odometer() and passing it 23_500 ❷.
# Finally, we call increment_odometer() and pass it 100 to add the
# 100 miles that we drove between buying the car and
# registering it.
