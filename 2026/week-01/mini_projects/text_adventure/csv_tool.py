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
