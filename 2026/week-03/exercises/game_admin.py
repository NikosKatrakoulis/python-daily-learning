# A game administrator is a special type of player. Create a class
# called Player with attributes such as username and level.
# Create a class called GameAdmin that inherits from Player.
# Add an attribute called admin_powers that stores a list of strings like
# "kick player", "ban player", "spawn items". Write a method called
# show_admin_powers() that displays all admin powers.
# Create an instance of GameAdmin, assign at least three powers,
# and call the method.

class Player:
    """A class representing a player."""

    def __init__(self, username, level):
        """Initialize the player."""
        self.username = username
        self.level = level

    def describe_player(self):
        """Display the summary of the player."""
        print(f"\nUsername:{self.username}")
        print(f"Level: {self.level}")


class GameAdmin(Player):
    """A player with administrative privileges."""

    def __init__(self, username, level):
        """initialize the game admin."""
        super().__init__(username, level)
        self.admin_powers = []

    def show_admin_powers(self):
        """Display the admin powers."""
        print("\nShowing admin powers:")
        for power in self.admin_powers:
            print(f"- {power}")


gameadmin = GameAdmin('mparmpasmpo', 68)
gameadmin.describe_player()

gameadmin.admin_powers = [
    "kick player",
    "ban player",
    "spawn items",
]

gameadmin.show_admin_powers()
