# Create a base class Character and a child class Warrior (inheritance).
# The Warrior should contain an Armor object with an attribute armor_level
# (default 1) and a method defense_points() that prints defense points
# based on the armor level. Add a method upgrade_armor() that upgrades
# the armor level to 3 if it’s not already. Create a warrior with
# default armor, call defense_points(), upgrade the armor, and call
# defense_points() again.

class Character:
    """A simple attempt to represent a game character."""

    def __init__(self, name, level):
        """Initialize attributes to describe a character."""
        self.name = name
        self.level = level


class Armor:
    """A simple attempt to model an armor for a warrior."""

    def __init__(self, armor_level=1):
        """Initialize the armor's attributes."""
        self.armor_level = armor_level

    def defense_points(self):
        """Print a statement describing the armor level."""
        print(f"The armor level of the warrior is {self.armor_level}.\n")

    def upgrade_armor(self):
        """Upgrade the armor level if possible."""
        if self.armor_level == 1:
            self.armor_level = 3
            print("Upgraded the armor level.")
        else:
            print("The armor level is already upgraded.")


class Warrior(Character):
    """Represent aspects of a character, specific to a warrior."""

    def __init__(self, name, level):
        """
        Initialize the attributes of the parent class.
        Then initialize the attributes specific to a warrior.
        """
        super().__init__(name, level)
        self.armor = Armor()


karabidas = Warrior('karabidas13', 88)
karabidas.armor.defense_points()

karabidas.armor.upgrade_armor()
karabidas.armor.defense_points()
