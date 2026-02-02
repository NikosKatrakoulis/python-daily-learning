"""
conversions.py

Contains all conversion logic for the unit converter.
It provides:
 - category-specific conversion functions(length, weight, temperature)
 - a dispatcher function that routes conversions based on category
"""


def convert_length(value, from_unit, to_unit):
    """Convert a length value between supported length units.

    Args:
        value: The numeric value to convert.
        from_unit: The unit of the input value (e.g. 'm', 'km', 'cm').
        to_unit: The unit to convert to (e.g. 'm', 'km', 'cm').

    Returns:
        The converted numeric value.

    Raises:
        ValueError: If from_unit or to_unit is not a supported length unit.
    """


def convert_weighy(value, from_unit, to_unit):
    """Convert a weight value between supported weight units.

    Args:
        value: The numeric value to convert.
        from_unit: The unit of the input value (e.g. 'g', 'kg').
        to_unit: The unit to convert to (e.g. 'g', 'kg').

    Returns:
        The converted numeric value.

    Raises:
        ValueError: If from_unit or to_unit is not a supported weight unit.
    """


def convert_temperature(value, from_unit, to_unit):
    """Convert a temperature value between Celsius and Fahrenheit.

    Args:
        value: The numeric value to convert.
        from_unit: The unit of the input value ('c' or 'f').
        to_unit: The unit to convert to ('c' or 'f').

    Returns:
        The converted numeric value.

    Raises:
        ValueError: If from_unit or to_unit is not a supported temperature unit.
    """


def convert(catergory, value, from_unit, to_unit):
    """Convert a value based on the selected category.

    This function acts as a dispatcher:
    - 'length' -> convert_length
    - 'weight' -> convert_weight
    - 'temperature' -> convert_temperature

    Args:
        category: The conversion category ('length', 'weight', 'temperature').
        value: The numeric value to convert.
        from_unit: The unit of the input value.
        to_unit: The unit to convert to.

    Returns:
        The converted numeric value.

    Raises:
        ValueError: If the category is unknown or units are invalid for that category. 
     """
