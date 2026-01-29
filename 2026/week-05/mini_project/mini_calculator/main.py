"""
main.py

Entry point for the mini calculator project.
It provides a simple CLI menu for performing operations and managing history.
"""

from calculator import Calculator, HistoryManager


def read_number(prompt: str) -> float:
    """Read a number from the user.

    Raises:
        ValueError: If the user input cannot be converted to a float.
    """
    text = input(prompt).strip()
    return float(text)


def print_menu() -> None:
    """Print the calculator menu."""
    print("\nCALCULATOR MENU")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Show history")
    print("6) Clear History")
    print("0) Exit")


def choice_to_operator(choice: str) -> str:
    """Convert a menu choice (1-4) into an operator symbol."""
    mapping = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
    }
    return mapping[choice]


def print_history(history: list[dict]) -> None:
    """Print calculation history in a readable format."""
    if not history:
        print("History is empty.")
        return

    print("\nHISTORY")
    for i, record in enumerate(history, start=1):
        a = record.get("a")
        b = record.get("b")
        op = record.get("op")
        result = record.get("result")
        print(f"{i}) {a} {op} {b} = {result}")


def main() -> None:
    """Run the calculator CLI program."""
    calc = Calculator()
    history_manager = HistoryManager()

    # Load history from disk at startup.
    history = history_manager.load()

    while True:
        print_menu()
        choice = input("\nChoose an option:").strip()

        # Exit
        if choice == "0":
            print("Goodbye!")
            break

        # Show history
        if choice == "5":
            print_history(history)
            continue

        # Clear History
        if choice == "6":
            history_manager.clear()
            history = []
            print("History cleared.")
            continue

        # Operations (1-4)
        if choice in {"1", "2", "3", "4"}:
            try:
                a = read_number("Enter the first number:")
                b = read_number("Enter the second number:")
                op = choice_to_operator(choice)

                result = calc.calculate(a, b, op)
                print(f"Result: {result}")

                # Update and save history
                history_manager.append(history, a, b, op, result)
                history_manager.save(history)
            except ValueError:
                print("Invalid number input. Please enter a valid number.")
            except ZeroDivisionError:
                print("Cannot divide by zero.")
            continue

        # Invalid choice
        print("Invalid choice. Please select a valid menu option.")


if __name__ == "__main__":
    main()
