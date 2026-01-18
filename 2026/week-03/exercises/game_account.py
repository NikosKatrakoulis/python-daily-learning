# Create a module called game_account.py. Inside this module,
# store the following classes: Player, GameAdmin (inherits from Player),
# AdminPowers (stores a list of admin powers). The GameAdmin class
# should include an AdminPowers instance. Create a separate file
# called my_game_account.py. Import the GameAdmin class, create an
# instance, assign several admin powers, and call the method that
# displays them to confirm everything is working correctly.

class Player:
    """A class representing a player."""

    def __init__(self, name, level):
        """Initialize the player."""
        self.name = name
        self.level = level

    def describe_player(self):
        """Display a summary of the player."""
        msg = f"The player's name is {self.name} and his level is {self.level}."
        print(msg)


class GameAdmin(Player):
    """A class representing a game admin."""

    def __init__(self, name, level):
        """Initialize the admin game."""
        super().__init__(name, level)
        self.powers = AdminPowers()


class AdminPowers:
    """A class representing the admin's powers."""

    def __init__(self, powers=[]):
        """Initialize the admin's powers."""
        self.powers = powers

    def show_powers(self):
        """Print the admin's powers."""
        print("\nAdmin's Powers:")
        for power in self.powers:
            print(f"- {power}")
