# Cities: Make a dictionary called cities. Use the names of three
# cities as keys in your dictionary. Create a dictionary of information
# about each city and include the country that the city is in, its
# approximate population, and one fact about that city. The keys for
# each city’s dictionary should be something like country, population,
# and fact. Print the name of each city and all of the information you
# have stored about it.

cities = {
    'athens': {
        'country': 'Greece',
        'population': 5_000_000,
        'fact': 'In athens the population is the half of the whole country.'
    },

    'nyc': {
        'country': 'USA',
        'population': 10_000_000,
        'fact': 'It is the capital of the west world.'
    },

    'zurich': {
        'country': 'Switzerland',
        'population': 436_000,
        'fact': 'It is the most expensive city in the world.'
    }
}

for city, city_info in cities.items():
    print(f"{city.title()}")
    print(f"Country: {city_info['country']}")
    print(f"Population: {city_info['population']}")
    print(f"Fact: {city_info['fact']}")
