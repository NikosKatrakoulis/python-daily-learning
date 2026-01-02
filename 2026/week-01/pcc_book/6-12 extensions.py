# Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example
# programs from this chapter, and extend it by adding new keys and values,
# changing the context of the program, or improving the formatting of the
# output.

cities = {
    'Athens': {
        'country': 'Greece',
        'population': 5_000_000,
        'language': ['Greek'],
        'landmarks': ['Parthenon', 'Acropolis'],
        'fact': 'The population is the half of the whole country.'
    },

    'Nyc': {
        'country': 'USA',
        'population': 10_000_000,
        'language': ['EnglishUS'],
        'landmarks': ['Central Park', 'Empire State Building', 'Brooklyn Bridge', 'Statue of Liberty'],
        'fact': 'It is the capital of the west world.'
    },

    'Zurich': {
        'country': 'Switzerland',
        'population': 436_000,
        'language': ['german', 'italian', 'france'],
        'landmarks': ['Kirche Fraumunster', 'Lindenhof'],
        'fact': 'It is the most expensive city in the world.'
    }
}

for city, city_info in cities.items():
    print(f"\nCity:{city}")
    print(f"Country: {city_info['country']}")
    print(f"Population: {city_info['population']}")
    print("Language: ")
    for language in city_info['language']:
        print(f"- {language}")
    print("Landmarks:")
    for landmark in city_info['landmarks']:
        print(f"- {landmark}")
    print(f"Fact: {city_info['fact']}")
