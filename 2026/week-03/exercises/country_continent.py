# Write a function called country_continent() that takes in the name of a
# country and its continent.The function should return a string formatted
# like this: "Greece, Europe". Call the function with at least three
# country–continent pairs, and print the returned values.

def country_continent(coutry, continent):
    """Return a string."""
    return f"\n{coutry.title()} is a country in {continent.title()} continent."


country = print(country_continent("greece", "europe"))
country = print(country_continent("japan", "asia"))
country = print(country_continent("brazil", "southern usa"))
