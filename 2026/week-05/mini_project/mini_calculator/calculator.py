"""
calculator.py

A beginner-friendly, class-based calculator module.
It provides:
- Operation classes(Add,Subtract,Multiply,Divide)
- A Calculator dispatcher that selects the correct operation
- A HistoryManager to load/save calculation history in JSON format
"""


class Operation:
    """Bass class for calculator operations.

    Child classes must define:
    - symbol: the operator string (e.g 'g')
    - execute(a, b): returns the result of the operation
    """

    def __init__(self, a, b):
        """Initialize the two numbers."""
        self.a = a
        self.b = b

    def execute(self, a, b):
        return


class Add(Operation):
    """Addition operation: returns a + b"""

    def __init__(self, a, b):
        super().__init__(a, b)

    def execute(self, a, b):
        return super().execute(a + b)


class Subtract(Operation):
    """Subtraction operation: returns a - b."""

    def __init__(self, a, b):
        super().__init__(a, b)

    def execute(self, a, b):
        return super().execute(a - b)


class Multiply(Operation):
    """Multiplication operation: returns a * b."""

    def __init__(self, a, b):
        super().__init__(a, b)

    def execute(self, a, b):
        return super().execute(a * b)


class Divide(Operation):
    """Division operation: returns a / b.

    Raises:
        ZeroDivisionError: if b is 0.
    """

    def __init__(self, a, b):
        super().__init__(a, b)

    def execute(self, a, b):
        if self.b == 0:
            return ZeroDivisionError
        return super().execute(a / b)


class Calculator:
    """Calculator dispatcher.

    Stores available operations and executes them based on an operator symbol.
    Example: calculate(5,2, '+') uses the Add operation
    """

    def __init__(self):
        self.dict = {
            "+": Add(),
            "-": Subtract(),
            "*": Multiply(),
            "/": Divide()
        }

    def available_operations(self, operators):
        self.operators = ["+", "-", "*", "/"]
        return self.operators


class HistoryManager:
    """Manages calculation history stored in a JSON file.

    Each history record looks like:
    {
      "a":5,
      "b":2,
      "op": "+",
      "result": 7
    }
    """

    def __init__(self, file_path="history.json"):
        pass

    def load(self):
        pass

    def save(self, history):
        pass

    def append(self, history, a, b, op, result):
        pass

    def clear(self):
        pass
