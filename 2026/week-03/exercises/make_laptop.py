# Write a function called make_laptop() that always receives a brand and a
# model. The function should then accept an arbitrary number of keyword
# arguments describing additional features (for example: ram, storage, color).
# Call the function with the required information and at least two
# extra name-value pairs. Print the dictionary that’s returned to confirm
# all information was stored correctly.

def make_laptop(brand, model, **features):
    """Make a dictionary representing a laptop."""
    laptop_dict = {
        'Brand': brand.title(),
        'Model': model.title()
    }
    for feature, value in features.items():
        laptop_dict[feature] = value
    return laptop_dict


dream_laptop = make_laptop('Apple', 'macBook Pro 16',
                           ram='48GB RAM', color='Black')
print(dream_laptop)
current_laptop = make_laptop(
    'asus', 'tuf gaming a16', ram='16GB Ram', storage="1TB")
print(current_laptop)
old_laptop = make_laptop('lenovo', 'ideaPad slim 3')
print(old_laptop)
