# Simulate how hard it is to guess a password. Create a list of possible
# characters (letters and numbers). Randomly generate a target password
# of 4 unique characters. Write a loop that keeps generating random
# passwords until one matches the target password. Count how many
# attempts it takes to guess correctly. Add a maximum number of attempts.
# Print the number of attempts and the final result.

from random import choice


def get_target_password(possibilities):
    """Return a password from a set of possibilities."""
    target_password = []

    while len(target_password) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in target_password:
            target_password.append(pulled_item)

    return target_password


def check_password(tried_password, right_password):
    for element in tried_password:
        if element not in right_password:
            return False

    return True


def make_password(possibilities):
    password = []

    while len(password) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in password:
            password.append(pulled_item)
    return password


possibilities = [
    1, 2, 3, 4, 5, 6, 7, 8, 9,
    'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x',
    'y', 'z']
target_password = get_target_password(possibilities)

tries = 0
found = False

max_tries = 1_000_000

while not found:
    new_try_password = make_password(possibilities)
    found = check_password(new_try_password, target_password)
    tries += 1
    if tries >= max_tries:
        break

if found:
    print(f"\nWe found the target password:")
    print(f"Your password: {new_try_password}")
    print(f"Target password: {target_password}")
    print(f"it only tooks {tries} tries to find it!")
else:
    print(f"Tried {tries} tries, without pulling the right password. :(")
    print(f"Your password: {new_try_password}")
    print(f"Target password: {target_password}")
