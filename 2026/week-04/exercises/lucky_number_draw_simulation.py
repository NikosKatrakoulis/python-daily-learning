# Simulate a lucky number draw. Create a list of possible numbers (1–20).
# Randomly generate a winning draw of 5 unique numbers. Write a loop that
# keeps generating random number draws until one matches the winning draw.
# Count how many attempts are needed to win. Set a maximum number of tries.
# Print the results, including whether a win was achieved.

from random import choice


def get_winning_draw(possibilities):
    winning_draw = []

    while len(winning_draw) < 5:
        pulled_item = choice(possibilities)

        if pulled_item not in winning_draw:
            winning_draw.append(pulled_item)

    return winning_draw


def check_draw(played_draw, winning_draw):

    for element in played_draw:
        if element not in winning_draw:
            return False

    return True


def make_randon_draw(possibilities):

    draw = []

    while len(draw) < 5:
        pulled_item = choice(possibilities)

        if pulled_item not in draw:
            draw.append(pulled_item)

    return draw


possibilities = [
    1, 2, 3, 4, 5, 6, 7, 8, 9,
    10, 11, 12, 13, 14, 15, 16,
    17, 18, 19, 20
]
winning_draw = get_winning_draw(possibilities)

plays = 0
won = False

max_tries = 1_000_000

while not won:
    new_draw = make_randon_draw(possibilities)
    won = check_draw(new_draw, winning_draw)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("\nWe have a winning draw:")
    print(f"Your draw: {new_draw}")
    print(f"Winning draw: {winning_draw}")
    print(f"It only tooks {plays} tries to find it!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_draw}")
    print(f"Winning ticket: {winning_draw}")
