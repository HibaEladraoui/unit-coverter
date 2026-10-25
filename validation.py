SUPPORTED_UNITS = {
    "length": ["m", "km", "cm", "mm", "mile", "ft", "inch"],
    "weight": ["kg", "g", "lb", "oz"],
    "temperature": ["C", "F", "K"],
}

ABSOLUTE_ZERO = {"C": -273.15, "F": -459.67, "K": 0}


def validate_value(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    return float(value)


def validate_unit(category, unit):
    if category not in SUPPORTED_UNITS:
        raise ValueError("Unknown category: " + str(category))
    if unit not in SUPPORTED_UNITS[category]:
        raise ValueError("Unsupported unit: " + str(unit))
    return unit


def validate_temperature(value, unit):
    validate_unit("temperature", unit)
    value = validate_value(value)
    if value < ABSOLUTE_ZERO[unit]:
        raise ValueError("Temperature is below absolute zero")
    return value
