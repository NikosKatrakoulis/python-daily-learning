# Simulate a mini bingo game. Create a list of possible numbers from 1 to 30.
# Randomly generate a winning bingo card containing 6 unique numbers.
# Write a loop that keeps generating random 6-number draws until one
# draw matches the winning card. Count how many attempts it took to win.
# Include a max number of tries to avoid running forever.
# Print the winning card, the final draw, and the number of attempts.

from random import choice


def get_winning_bingo_card(possibilities):
    winning_bingo_card = []

    while len(winning_bingo_card) < 6:
        pulled_item = choice(possibilities)

        if pulled_item not in winning_bingo_card:
            winning_bingo_card.append(pulled_item)

    return winning_bingo_card


def check_winning_bingo_card(played_bingo_card, winning_bingo_card):

    for element in played_bingo_card:
        if element not in winning_bingo_card:
            return False

    return True


def make_random_bingo_card(possibilities):
    bingo_draw = []

    while len(bingo_draw) < 6:
        pulled_item = choice(possibilities)

        if pulled_item not in bingo_draw:
            bingo_draw.append(pulled_item)

    return bingo_draw


possibilities = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
]
winning_bingo_card = get_winning_bingo_card(possibilities)

plays = 0
won = False

max_tries = 1_000_000

while not won:
    new_draw = make_random_bingo_card(possibilities)
    won = check_winning_bingo_card(new_draw, winning_bingo_card)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("\nWe have a winning bingo card:")
    print(f"Your bingo card: {new_draw}")
    print(f"Winning bingo card: {winning_bingo_card}")
    print(f"It only tooks {plays} tries to find it.")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your bingo card: {new_draw}")
    print(f"Winning bingo car: {winning_bingo_card}")
