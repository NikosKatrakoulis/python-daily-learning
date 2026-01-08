# You can import as many classes as you need into a program
# file. If we want to make a regular car and an electric car in
# the same file, we need to import both classes, Car and
# ElectricCar:

# from car import Car
# from electric_car import ElectricCar

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# You import multiple classes from a module by separating
# each class with a comma ❶. Once you’ve imported the
# necessary classes, you’re free to make as many instances of
# each class as you need.

# You can also import an entire module and then access the
# classes you need using dot notation. This approach is simple
# and results in code that is easy to read. Because every call
# that creates an instance of a class includes the module
# name, you won’t have naming conflicts with any names
# used in the current file.
# Here’s what it looks like to import the entire car module
# and then create a regular car and an electric car:

# import car

# my_mustang = car.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())


# You can use
# aliases when importing classes as well.
# As an example, consider a program where you want to
# make a bunch of electric cars. It might get tedious to type
# (and read) ElectricCar over and over again. You can give
# ElectricCar an alias in the import statement.
# You can also give a module an alias. Here’s how to import
# the entire electric_car module using an alias.


from car import Car
from electric_car import ElectricCar as EC
# import electric_car as ec

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = EC('nissan', 'leaf', 2024)
# my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
