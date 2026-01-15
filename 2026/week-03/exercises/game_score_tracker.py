# Create a class called Player. Add attributes like name and level.
# Add an attribute called score with a default value of 0.
# Write a method called increase_score() that increments score by 1.
# Write a method called reset_score() that resets score to 0.
# Create an instance of Player, call increase_score() several times,
# print the score to confirm it increments properly, then call
# reset_score() and print it again.

class Player:
    """A class representing a player."""

    def __init__(self, name, level):
        """Initialize the player."""
        self.name = name.title()
        self.level = level
        self.score = 0

    def describe_player(self):
        """Displat a summary of the player's information."""
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")

    def greet_player(self):
        """Display a personalized greeting."""
        print(f"\nHello {self.name}, ready to score?")

    def increase_score(self):
        """Increasing the number of the score."""
        self.score += 1

    def reset_score(self):
        """Resetting the number of the score."""
        self.score = 0


player = Player('cristiano ronaldo', 94)
player.describe_player()
player.greet_player()

print("\nAdding 6 goals to the score...")
player.increase_score()
player.increase_score()
player.increase_score()
player.increase_score()
player.increase_score()
player.increase_score()
print(f"    Score number: {player.score}")

print("\nResetting the score number...")
player.reset_score()
print(f"    Score number {player.score}")
