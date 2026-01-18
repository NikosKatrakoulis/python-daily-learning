# Create a simulation of a dice jackpot game. Create a list of possible
# dice values (1–6). Randomly generate a winning combination of 3
# unique numbers.Create a loop that keeps rolling random dice
# combinations until your roll matches the winning combination.
# Count how many rolls it takes to win.
# Set a maximum number of attempts to avoid an infinite loop.
# Print how many tries were needed to win, or report failure if the
# limit is reached.

from random import choice


def get_winning_combination(possibilites):
    """Return a winning combination from a set of possibilities."""
    winning_combination = []

    # We don't want to repeat winning numbers, so we'll use a while loop.
    while len(winning_combination) < 3:
        pulled_item = choice(possibilites)

        # Only add the pulled item to the winning combination if it hasn't
        # already been pulled
        if pulled_item not in winning_combination:
            winning_combination.append(pulled_item)

    return winning_combination


def check_combination(played_combination, winning_combination):
    # Check all elements in the played combination. If any are not in the
    # winning combination return False.
    for element in played_combination:
        if element not in winning_combination:
            return False

    # We must have a winning combination
    return True


def make_random_combination(possibilities):
    """Return a random combination from a set of possibilities."""
    combination = []

    while len(combination) < 3:
        pulled_item = choice(possibilities)

        if pulled_item not in combination:
            combination.append(pulled_item)

    return combination


possibilities = [1, 2, 3, 4, 5, 6]
winning_combination = get_winning_combination(possibilities)

plays = 0
won = False

max_tries = 1_000_000

while not won:
    new_combination = make_random_combination(possibilities)
    won = check_combination(new_combination, winning_combination)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning combination:")
    print(f"Your combination: {new_combination}")
    print(f"Winning combination: {winning_combination}")
    print(f"It only tooks {plays} times to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your combination: {new_combination}")
    print(f"Winning combination: {winning_combination}")
