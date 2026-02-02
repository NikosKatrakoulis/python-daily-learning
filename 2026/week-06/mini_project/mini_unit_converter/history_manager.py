"""
history_manager.py

Handles loading, saving, appending and clearing conversion history stored in JSON.
"""


class HistoryManager:
    """Manages conversion history stored in a JSON file.

    Each history record looks like:
    {
        "category": "length",
        "value": 1500,
        "from_unit": "m",
        "to_unit": "km",
        "result": 1.5,
    }
    """

    def __init__(self):
        """Create a history manager that reads/writes to the given JSON file."""

    def load():
        """Load and return the history list from the JSON file.

        Returns:
            A list of history records. If the file does not exit or is invalid,
            returns an empty list.
        """

    def save(history):
        """Save the given history list to the JSON file.

        Args:
            history: A list of history records (each record is a dict).
        """

    def append(history, record):
        """Append a new history record to the history list and return updated list.

        Args:
            history: The current history list.
            record: A single conversion record to add.

        Returns:
            The updated history list.
        """

    def clear():
        """Clear the history file (save an empty list)."""
