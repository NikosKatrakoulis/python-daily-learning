# Write a function called describe_landmark() that accepts the name of a
# landmark and the city it is located in. Give the city parameter a default
# value. The function should print a sentence describing the landmark’s
# location. Call the function three times, with at least one call using a
# city different from the default.

def describe_landmark(landmark, city="athens"):
    """Describe a landmark."""
    msg = f"\n{landmark.title()} is a landmark located in {city.title()}."
    print(msg)


describe_landmark("parthenon")
describe_landmark("acropolis")
describe_landmark("statue of liberty", "nyc")
