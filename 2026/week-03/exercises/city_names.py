# Write a function called city_country() that takes in the name of a city
# and its country. The function should return a string formatted like this:
# 'Santiago, Chile'. Call your function with at least three city-country pairs,
# and print the values that are returned.

def city_country(city, country):
    """Return a string."""
    return f"{city.title()}, {country.title()}"


city = city_country("miami", "florida")
print(city)
city = city_country("zurich", "switzerland")
print(city)
city = city_country("amsterdam", "netherlands")
print(city)
