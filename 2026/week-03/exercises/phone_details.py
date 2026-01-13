# Write a function called make_phone() that always receives a brand and a
# model.Accept any number of keyword arguments representing phone features
# (such as color, storage, has_5g). Call the function with the required
# arguments and two additional options.Print the resulting dictionary.

def make_phone(brand, model, **features):
    """Make a dictionary representing a phone."""
    phone_dict = {
        'Brand': brand.title(),
        'Model': model.title()
    }
    for feauture, value in features.items():
        phone_dict[feauture] = value
    return phone_dict


dream_phone = make_phone('apple', 'iPhone 16 pro max',
                         color='Deep Blue', storage='1TB', has_5g=True)
print(dream_phone)
current_phone = make_phone(
    'apple', 'iPhone 6s', color='gold', storage='128GB', has_5g=False)
print(current_phone)
old_phone = make_phone('nokia', '3300')
print(old_phone)
