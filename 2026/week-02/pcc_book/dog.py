# Each instance created from the Dog class will store a name and
# an age, and we’ll give each dog the ability to sit() and
# roll_over():

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# The two variables defined in the body of the __init__()
# method each have the prefix self. Any variable prefixed
# with self is available to every method in the class, and we’ll
# also be able to access these variables through any instance
# created from the class. The line self.name = name takes the
# value associated with the parameter name and assigns it to
# the variable name, which is then attached to the instance
# being created. The same process happens with self.age =
# age. Variables that are accessible through instances like this
# are called attributes.


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# To access the attributes of an instance, you use dot
# notation. Dot notation is used often in Python. This syntax
# demonstrates how Python finds an attribute’s value. Here,
# Python looks at the instance my_dog and then finds the
# attribute name associated with my_dog. This is the same
# attribute referred to as self.name in the class Dog. We use the
# same approach to work with the attribute age.

# After we can use dot notation to call any method defined in Dog.
# Let’s make our dog sit and roll over:

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

# You can create as many instances from a class as you need.
# Let’s create a second dog called your_dog.In this example we
# create a dog named Willie and a dog
# named Lucy. Each dog is a separate instance with its own
# set of attributes, capable of the same set of actions:

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
