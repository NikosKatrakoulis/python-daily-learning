# People: Start with the program you wrote for Exercise 6-1 (page 98).
#  Make two new dictionaries representing different people, and store
#  all three dictionaries in a list called people. Loop through your
#  list of people. As you loop through the list, print everything you
#  know about each person.


for person in range(3):
    person_01 = {
        'first_name': 'giorgos',
        'last_name': 'papadopoulos',
        'age': 5,
        'city': 'athens',
    }

    person_02 = {
        'first_name': 'giannis',
        'last_name': 'vasilakis',
        'age': 19,
        'city': 'atra',
    }
    person_03 = {
        'first_name': 'panagiotis',
        'last_name': 'pavlidis',
        'age': 52,
        'city': 'alexandroupoli',
    }


people = [person_01, person_02, person_03]

for person in people:
    print("\nPerson Information")
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
