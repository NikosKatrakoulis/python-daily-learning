# Simulate cracking a 3-digit lock. Create a list of possible digits (0–9).
# Randomly generate a target combination of 3 digits. Write a loop that
# keeps generating random 3-digit combinations until one matches the target.
# Count how many tries were needed. Add a maximum tries limit.
# Print the target combination, the successful guess, and the number of tries.

from random import choice


def get_cracked_log(possibilities):
    cracked_lock = []

    while len(cracked_lock) < 3:
        pulled_item = choice(possibilities)

        if pulled_item not in cracked_lock:
            cracked_lock.append(pulled_item)

    return cracked_lock


def check_cracking_lock(tried_cracking_lock, cracked_lock):

    for element in tried_cracking_lock:
        if element not in cracked_lock:
            return False

    return True


def make_cracking_lock(possibilities):
    lock = []

    while len(lock) < 3:
        pulled_item = choice(possibilities)

        if pulled_item not in lock:
            lock.append(pulled_item)

    return lock


possibilities = [
    1, 2, 3, 4, 5, 6, 7, 8, 9
]
cracked_lock = get_cracked_log(possibilities)

plays = 0
won = False

max_tries = 100

while not won:
    new_try = make_cracking_lock(possibilities)
    won = check_cracking_lock(new_try, cracked_lock)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("\nWe found the 3-digit code:")
    print(f"Your code: {new_try}")
    print(f"Locker code: {cracked_lock}")
    print(f"It only tooks {plays} tries to find it.")
else:
    print(f"Tried {plays} times, without finding the code. :(")
    print(f"Your code: {new_try}")
    print(f"Locker code: {cracked_lock}")
