# Make a class called Coin with one attribute called sides, which has a
# default value of 2 (Heads/Tails). Write a method called flip() that
# returns a random result: "Heads" or "Tails". Make a coin with the
# default settings and flip it 10 times. Then make a “special coin”
# that returns one of 3 outcomes (for example: "Heads", "Tails", "Edge").
# Flip it 10 times. Print the results of each set of 10 flips.

from random import choice


class Coin:
    """Represent a coin, which can be fliped."""

    def __init__(self, sides=None):
        """Initialize the coin."""
        if sides is None:
            self.sides = ["Heads", "Tails"]
        else:
            self.sides = sides

    def flip(self):
        """Return a side between Heads or Tails."""
        return choice(self.sides)


coin = Coin()

results = []
for side in range(10):
    result = coin.flip()
    results.append(result)
print("10 flips of a two-sided coin:")
print(results)

special_coin = Coin(["Heads", "Tails", "Edge"])

results = []
for flip in range(10):
    result = special_coin.flip()
    results.append(result)
print("\n10 flips of a three-sided coin:")
print(results)
