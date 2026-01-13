# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other
# name-value pairs, such as a color or an optional feature.
# Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary that's returned to make sure all the information
# was stored correctly.


def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'Manufacturer': manufacturer.title(),
        'Model': model.title(),
    }

    for option, value in options.items():
        car_dict[option] = value
    return car_dict


car = make_car('subaru', 'outback', color='blue', tow_packages=True)
print(car)

my_old_car = make_car('fiat', '500', color='white', two_packages=False)
print(my_old_car)
