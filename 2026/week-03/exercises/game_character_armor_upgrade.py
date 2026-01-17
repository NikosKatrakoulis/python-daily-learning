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


class Warrior(Character):
    """Represent aspects of a character, specific to a warrior."""

    def __init__(self, name, level):
        """
        Initialize the attributes of the parent class.
        Then initialize the attributes specific to a warrior.
        """
        super().__init__(name, level)
        self.armor = Armor()
