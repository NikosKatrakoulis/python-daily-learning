cities = ['nea peramos', 'megara', 'athina', 'thessaloniki']

print(f"I grew up in {cities[0].title()}.")
cities.append('patra')
print(cities)

cities.insert(4, 'volos')
print(cities)

del cities[3]
print(cities)

city1 = cities.pop()
print(f"I have never visited {city1.title()}.")
print(cities)

city2 = 'athina'
cities.remove(city2)
print(f"I dont want to live in {city2.title()}.")
print(cities)

print(sorted(cities))
cities.reverse()
print(cities)

cities.sort()
print(cities)
