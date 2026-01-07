# You don’t always have to start from scratch when writing a
# class. If the class you’re writing is a specialized version of
# another class you wrote, you can use inheritance. When one
# class inherits from another, it takes on the attributes and
# methods of the first class. The original class is called the
# parent class, and the new class is the child class. The child
# class can inherit any or all of the attributes and methods of
# its parent class, but it’s also free to define new attributes
# and methods of its own.

# An electric car
# is just a specific kind of car, so we can base our new
# ElectricCar class on the Car class we wrote earlier. Then we’ll
# only have to write code for the attributes and behaviors
# specific to electric cars.
# Let’s start by making a simple version of the ElectricCar
# class, which does everything the Car class does:

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


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())


# We start with Car ❶. When you create a child class, the
# parent class must be part of the current file and must
# appear before the child class in the file. We then define the
# child class, ElectricCar ❷. The name of the parent class must
# be included in parentheses in the definition of a child class.
# The __init__() method takes in the information required to
# make a Car instance ❸.
# The super() function ❹ is a special function that allows you
# to call a method from the parent class. This line tells Python
# to call the __init__() method from Car, which gives an
# ElectricCar instance all the attributes defined in that
# method. The name super comes from a convention of
# calling the parent class a superclass and the child class a
# subclass.
# We test whether inheritance is working properly by trying
# to create an electric car with the same kind of information
# we’d provide when making a regular car. We make an
# instance of the ElectricCar class and assign it to my_leaf ❺.
# This line calls the __init__() method defined in ElectricCar,
# which in turn tells Python to call the __init__() method
# defined in the parent class Car. We provide the arguments
# 'nissan', 'leaf', and 2024.
# Aside from __init__(), there are no attributes or methods
# yet that are particular to an electric car. At this point we’re
# just making sure the electric car has the appropriate Car
# behaviors.
# The ElectricCar instance works just like an instance of Car,
# so now we can begin defining attributes and methods
# specific to electric cars.

# Once you have a child class that inherits from a parent
# class, you can add any new attributes and methods
# necessary to differentiate the child class from the parent
# class.
# Let’s add an attribute that’s specific to electric cars (a
# battery, for example) and a method to report on this
# attribute. We’ll store the battery size and write a method
# that prints a description of the battery:

# class Car:
#     --snip--

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car. 
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size} -kWh battery.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()

# An attribute or method that
# could belong to any car, rather than one that’s specific to an
# electric car, should be added to the Car class instead of the
# ElectricCar class. Then anyone who uses the Car class will
# have that functionality available as well, and the ElectricCar
# class will only contain code for the information and behavior
# specific to electric vehicles.


# You can override any method from the parent class that
# doesn’t fit what you’re trying to model with the child class.
# To do this, you define a method in the child class with the
# same name as the method you want to override in the
# parent class. Python will disregard the parent class method
# and only pay attention to the method you define in the child
# class.
# Say the class Car had a method called fill_gas_tank(). This
# method is meaningless for an all-electric vehicle, so you
# might want to override this method. Here’s one way to do
# that:


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car. 
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size} -kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")


# When modeling something from the real world in code, you
# may find that you’re adding more and more detail to a class.
# You’ll find that you have a growing list of attributes and
# methods and that your files are becoming lengthy. In these
# situations, you might recognize that part of one class can be
# written as a separate class. You can break your large class
# into smaller classes that work together; this approach is
# called composition.
# For example, if we continue adding detail to the
# ElectricCar class, we might notice that we’re adding many
# attributes and methods specific to the car’s battery. When
# we see this happening, we can stop and move those
# attributes and methods to a separate class called Battery.
# Then we can use a Battery instance as an attribute in the
# ElectricCar class:

# class Car:
#     --snip--

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parrent class.
           Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

# We define a new class called Battery that doesn’t inherit
# from any other class. The __init__() method  has one
# parameter, battery_size, in addition to self. This is an
# optional parameter that sets the battery’s size to 40 if no
# value is provided. The method describe_battery() has been
# moved to this class as well .
# In the ElectricCar class, we now add an attribute called
# self.battery . This line tells Python to create a new
# instance of Battery (with a default size of 40, because we’re
# not specifying a value) and assign that instance to the
# attribute self.battery. This will happen every time the
# __init__() method is called; any ElectricCar instance will now
# have a Battery instance created automatically.
# We create an electric car and assign it to the variable
# my_leaf. When we want to describe the battery, we need to
# work through the car’s battery attribute.


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

        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""

        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car. 
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
