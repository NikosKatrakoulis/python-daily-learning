# Write a function called describe_country() that accepts the name of a
# country and its continent. Give the continent parameter a default value.
# The function should print a simple sentence describing where the country
# is located. Call the function for three different countries, at least one
# of which is not in the default continent.

def describe_country(country, contintent="Europe"):
    """Describe a country."""
    msg = f"\n{country.title()} is in {contintent.title()}."
    print(msg)


describe_country("Greece")
describe_country("Portugal")
describe_country(country="japan", contintent="asia")
