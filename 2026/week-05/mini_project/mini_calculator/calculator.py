"""
calculator.py

A beginner-friendly, class-based calculator module.
It provides:
- Operation classes(Add,Subtract,Multiply,Divide)
- A Calculator dispatcher that selects the correct operation
- A HistoryManager to load/save calculation history in JSON format
"""


import json
from pathlib import Path


class Operation:
    """Base class for calculator operations.

    Child classes must define:
    - symbol: the operator string (e.g '+')
    - execute(a, b): returns the result of the operation
    """

    # Each child class should override this with  real symbol (e.g. "+")
    symbol: str = " "

    def execute(self, a: float, b: float) -> float:
        """Execute the operator and return the result.

        Raises:
            NotImplementedError: If a child class does not implement this method.
        """

        raise NotImplementedError("Child classes must implement execute().")


class Add(Operation):
    """Addition operation: returns a + b"""

    symbol = "+"

    def execute(self, a: float, b: float) -> float:
        """Return a + b."""
        return a + b


class Subtract(Operation):
    """Subtraction operation: returns a - b."""

    symbol = "-"

    def execute(self, a: float, b: float) -> float:
        """Return a - b."""
        return a - b


class Multiply(Operation):
    """Multiplication operation: returns a * b."""

    symbol = "*"

    def execute(self, a: float, b: float) -> float:
        """Return a * b."""
        return a * b


class Divide(Operation):
    """Division operation: returns a / b.

    Raises:
        ZeroDivisionError: if b is 0.
    """

    symbol = "/"

    def execute(self, a: float, b: float) -> float:
        """Return a / b.

        Raises:
            ZeroDivisionError: if b is 0.
        """

        if b == 0:
            # We raise an exception so the caller(main menu) can handle it nicely.
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


class Calculator:
    """Calculator dispatcher.

    Stores available operations and executes them based on an operator symbol.
    Example: calculate(5,2, '+') uses the Add operation
    """

    def __init__(self) -> None:
        # Map each operator symbol to the operation object that can execute it.
        self.operations = {
            Add.symbol: Add(),
            Subtract.symbol: Subtract(),
            Multiply.symbol: Multiply(),
            Divide.symbol: Divide()
        }

    def available_operations(self) -> list[str]:
        """Return a list of available operation symbols (e.g. ['+', '-', '*', '/'])."""
        return list(self.operations.keys())

    def calculate(self, a: float, b: float, op: str) -> float:
        """Calculate a result using the given operator symbol.

        Raises:
            ValueError: If op is not a supported operation.
        """

        if op not in self.operations:
            raise ValueError("Invalid operation.")
        return self.operations[op].execute(a, b)


class HistoryManager:
    """Manages calculation history stored in  JSON file.

    Each history record looks like:
    {
      "":5,
      "b":2,
      "op": "+",
      "result": 7
    }
    """

    def __init__(self, file_path: str = "history.json") -> None:
        """Create a history manager that reads/writes to the given JSON file."""
        self.file_path = Path(file_path)

    def load(self) -> list[dict]:
        """Load and return the history list from the JSON file.

        Returns:
            A list of history records. If the file does not exist or is invalid
            returns an empty list.
        """
        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)

            # We expect a list. If something else is stored, return empty list
            if isinstance(data, list):
                return data
            return []
        except (json.JSONDecodeError, OSError):
            return []

    def save(self, history: list[dict]) -> None:
        """Save the given history list to the JSON file."""
        with self.file_path.open("w", encoding="utf-8") as f:
            json.dump(history, f, indent=2)

    def append(self, history: list[dict], a: float, b: float, op: str, result: float) -> list[dict]:
        """Append a new calculation record to history and return the updated list."""
        record = {"a": a, "b": b, "op": op, "result": result}
        history.append(record)
        return history

    def clear(self) -> None:
        """Clear the history file (save an empty list.)"""
        self.save([])
