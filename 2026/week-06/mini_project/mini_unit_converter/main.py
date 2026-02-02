"""
main.py

Entry point for the unit converter project.
It provides a simple CLI menu to:
  - perform unit conversions
  - view and clear conversion history stored in JSON
  """


def print_menu():
    """Print the main menu for the unit converter CLI."""


def read_number(prompt):
    """Read a numeric value from the user.

    Args:
        prompt: The text shown to the user.

    Returns:
        The number entered by the user as a float.

    Raises:
        ValueError: If the input cannot be converted to a float.
    """


def read_unit(prompt):
    """Read a unit string from the user and normalize it.

    Args:
        prompt: the text shown to the user.

    Returns:
        A normalized unit string (lowercase, stripped).
    """


def print_history(history):
    """Print conversion history in a readable format.

    Args:
        history: A list of history records (each record is a dict).
    """


def main():
    """Run the unit converter CLI program."""
