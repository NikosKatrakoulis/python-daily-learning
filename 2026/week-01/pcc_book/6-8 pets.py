# Pets: Make several dictionaries, where each dictionary represents
# a different pet. In each dictionary, include the kind of animal and
# the owner’s name. Store these dictionaries in a list called pets.
# Next, loop through your list and as you do, print everything you
# know about each pet.

pet_01 = {
    'animal': 'dog',
    'ownername': 'dimitris',
}

pet_02 = {
    'animal': 'cat',
    'ownername': 'niki',
}

pet_03 = {
    'animal': 'rabbit',
    'ownername': 'foteini',
}

pets = [pet_01, pet_02, pet_03]

for pet in pets:
    print("\nPet Information:")
    print(f"Animal: {pet['animal'].title()}")
    print(f"Ownername: {pet['ownername'].title()}")
