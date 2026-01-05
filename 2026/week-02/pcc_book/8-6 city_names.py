# City Names: Write a function called city_country() that takes in the
# name of a city and its country. The function should return a string formatted
# like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.

def city_country(city, country):
    return f"{city.title()}, {country.title()}"


location1 = city_country(city='athens', country='greece')
location2 = city_country(city='amsterdam', country='the netherlands')
location3 = city_country(city='zurich', country='switzerland')
print(location1)
print(location2)
print(location3)
