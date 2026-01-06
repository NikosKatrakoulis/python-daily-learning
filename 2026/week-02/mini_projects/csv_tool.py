"""
csv_tool.py

A beginner-friendly CSV Tool using Python's standard library.
Features:
    - Load CSV
    - Preview rows
    - Show columns
    - Filter rows by "column equals value"
    - Select columns
    - Sort by column(numeric when possible)
    - Add a new column (copy or simple numeric rule)
    - Save to a new CSV file
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# --------------------------------
# Helpers: small utility functions
# --------------------------------


def file_exists(path_str: str) -> bool:
    """Check if a path points to an existing file."""
    return Path(path_str).is_file()


def try_parse_number(value: str) -> Optional[float]:
    """
    Try to convert a string to a number.
    If it works, return the number.
    If it fails, return None.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def print_divider() -> None:
    """Print a simple divider line."""
    print("-" * 60)


def safe_input(prompt: str) -> str:
    """
    Read user input safely(strip spaces).
    If user just presses Enter, return empty string.
    """
    return input(prompt).strip()

# -----------------------------
# CSV Read/Write
# -----------------------------


def load_csv(file_path: str) -> Tuple[List[str], List[Dict[str, str]]]:
    """
    Load a CSV file into memory.

    Returns:
        headers: list of column names
        rows: list of dicts, where each dict is one row ( column -> value)
        """
    path = Path(file_path)

    # Open with newLine="" to avoid extra blank lines on Windows
    with path.open(mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        # DictReader automaticallu read headers from the first row
        headers = reader.fieldnames or []
        rows = list(reader)

    return headers, rows


def save_csv(file_path: str, headers: List[str], rows: List[Dict[str, str]]) -> None:
    """
    Save rows to a CSV file using the provided headers.
    """

    path = Path(file_path)

    # Make sure parent folder exists
    if path.parent:
        path.parent.mkdir(parents=True, exist_ok=True)

    with path.open(mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)

        # Write header now
        writer.writeheader()

        # Write each data row
        for row in rows:
            # Ensure missing columns are written as empty strings
            clean_row = {h: row.get(h, "") for h in headers}
            writer.writerow(clean_row)


# -----------------------------
# Operations on data (rows)
# -----------------------------

def preview_rows(headers: List[str], rows: List[Dict[str, str]], n: int = 5) -> None:
    """
    Print the first N rows in a simple table-like format.
    """

    if not headers:
        print("No headers found.")
        return

    if not rows:
        print("No rows to display.")
        return

    # Determine how many rows we will actually show
    n = max(1, min(n, len(rows)))

    print_divider()
    print(f"Previewing first {n} row(s):")
    print_divider()

    # Print headers
    print(" | ".join(headers))
    print_divider()

    # Print rows
    for i in range(n):
        row = rows[i]
        values = [row.get(h, "")for h in headers]
        print(" | ".join(values))

    print_divider()


def show_columns(headers: List[str]) -> None:
    """Print all column names."""
    if not headers:
        print("No columns found.")
        return

    print_divider()
    print("Columns:")
    for h in headers:
        print(f"  -{h}")
    print_divider()


def filter_rows_equals(rows: List[Dict[str, str]], column: str, value: str) -> List[Dict[str, str]]:
    """
    Keep only rows where row[column] == value(exact match).
    """

    filtered = []
    for row in rows:
        if row.get(column, "") == value:
            filtered.append(row)
        return filtered


def select_columns(headers: List[str], rows: List[Dict[str, str]], selected: List[str]) -> Tuple[List[str], List[Dict[str, str]]]:
    """
    Keep only the selected columns.

    Returns new headers, new_rows
    """
    new_headers = [c for c in selected if c in headers]
    new_rows = []

    for row in rows:
        new_row = {c: row.get(c, "")for c in new_headers}
        new_rows.append(new_row)

    return new_headers, new_rows


def sort_rows(rows: List[Dict[str, str]], column: str, descending: bool = False):
    """
    Sort rows by a column.
    If values look like numbers, sort numerically.
    Otherwise, sort as strings.
    """

    def sort_key(row: Dict[str, str]):
        raw = row.get(column, "")
        num = try_parse_number(raw)
        # If it's a number, sort by number; otherwise by lowercase string
        return (0, num) if num is not None else (1, raw.lower())

    return sorted(rows, key=sort_key, reverse=descending)


def add_column_copy(headers: List[str], rows: List[Dict[str, str]], new_col: str, source_col: str) -> Tuple[List[str], List[Dict[str, str]]]:
    """
    Add a new column by copying values from an existing column.
    """

    if new_col not in headers:
        headers = headers + [new_col]

    for row in rows:
        row[new_col] = row.get(source_col, "")

    return headers, rows


def add_column_numeric_rule(
    headers: List[str],
    rows: List[Dict[str, str]],
    new_col: str,
    source_col: str,
    operator: str,
    threshold: float,
) -> Tuple[List[str], List[Dict[str, str]]]:
    """
    Add a new column based on a simple numerice rule, e.g.:
    - age >= 18 -> "YES"
    - price < 10 -> "YES"
    If the source value in not numeric, result becomes "NO" .
    """

    if new_col not in headers:
        headers = headers + [new_col]

    for row in rows:
        raw_value = row.get(source_col, "")
        num = try_parse_number(raw_value)

        # If we cannot pase a number, rule fails
        if num is None:
            row[new_col] = "NO"
            continue

        ok = False
        if operator == ">":
            ok = num > threshold
        elif operator == ">=":
            ok = num >= threshold
        elif operator == "<":
            ok = num < threshold
        elif operator == "<=":
            ok = num <= threshold
        elif operator == "==":
            ok = num = threshold
        else:
            ok = False

        row[new_col] = "YES" if ok else "NO"

    return headers, rows


# -----------------------------
# CLI Menu (the "brain" that asks user what to do)
# -----------------------------

def print_menu() -> None:
    """Print the menu options."""
    print("\nCSV TOOL MENU")
    print("1) Load CSV")
    print("2) Preview rows")
    print("3) Show columns")
    print("4) Filter rows (column == value)")
    print("5) Select columns")
    print("6) Sort rows")
    print("7) Add column (copy or rule)")
    print("8) Save CSV")
    print("9) Reset (reload original data)")
    print("10) Quit")


def main() -> None:
    # These variables hold our current working dataset
    headers: List[str] = []
    rows: List[Dict[str, str]] = []

    # These keep a copy of the original Loaded dataset
    original_headers: List[str] = []
    original_rows: List[Dict[str, str]] = []

    print("Welcome to the CSV Tool!")
    print("This tool helps you load, inspect,transform and save CSV files.")

    while True:
        print_menu()
        choice = safe_input("\mChoose an option: ")

        # Option 0: Quit

        if choice == "0":
            print("Goodbye!")
            break

        # Option 1: Load CSV

        elif choice == "1":
            file_path = safe_input("Enter CSV file path: ")

            if not file_exists(file_path):
                print("File not found. Please try again.")
                continue

            try:
                headers, rows = load_csv(file_path)
                original_headers = headers.copy()
                original_rows = [r.copy() for r in rows]  # deep-ish copy

                print(
                    f"Loaded {len(rows)} row(s) with {len(headers)} column(s).")
            except Exception as e:
                print(f"Failed to load CSV: {e}")

        # Option 2: Preview rows

        elif choice == "2":
            if not headers:
                print("No CSV loaded yet. Load a file first.")
                continue

            n_str = safe_input("How many rows to preview? (default 5): ")
            n = 5
            if n_str:
                maybe = try_parse_number(n_str)
                if maybe is not None and maybe > 0:
                    n = int(maybe)

            preview_rows(headers, rows, n=n)
