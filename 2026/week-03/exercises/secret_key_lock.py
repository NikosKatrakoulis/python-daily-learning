# Make a tuple containing 15 items: a mix of numbers (1–10) and letters
# (at least 5 letters). Randomly select 3 unique items to create a
# “secret key”. Print each selected item as it is chosen, and then
# print the final secret key. Print a message saying that any key
# matching the secret key unlocks the door.

from random import choice

possibilities = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

secret_key = []
print("Let's see what is the secret key to open the door:")

while len(secret_key) < 3:
    pulled_item = choice(possibilities)

    if pulled_item not in secret_key:
        print(f"    We pulled a {pulled_item}")
        secret_key.append(pulled_item)

print(f"Final Secret Key {secret_key}")
print(f"\nAny key matching the {secret_key} unlocks the door.")
