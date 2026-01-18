# Create a class called Car and store it in a file called car.py.
# The class should store information such as the car’s make, model,
# and year, and include a method that prints a descriptive name of the car.
# Create a second file called my_car.py.
# Import the Car class, create an instance, and call the descriptive
# method to confirm that the import statement works properly.

from car import Car

my_new_car = Car('toyota', 'yaris')
my_new_car.describe_car()
