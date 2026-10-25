
LENGTH_TO_METERS = {
    "m": 1,
    "km": 1000,
    "cm": 0.01,
    "mi": 1609.344,
}

WEIGHT_TO_GRAMS = {
    "g": 1,
    "kg": 1000,
    "lb": 453.59237,
}


def convert_length(value, from_unit, to_unit):
    """Convert a length between supported units."""
    if from_unit not in LENGTH_TO_METERS or to_unit not in LENGTH_TO_METERS:
        raise ValueError("Unsupported length unit.")

    return value * LENGTH_TO_METERS[from_unit] / LENGTH_TO_METERS[to_unit]


def convert_weight(value, from_unit, to_unit):
    """Convert a weight between supported units."""
    if from_unit not in WEIGHT_TO_GRAMS or to_unit not in WEIGHT_TO_GRAMS:
        raise ValueError("Unsupported weight unit.")

    return value * WEIGHT_TO_GRAMS[from_unit] / WEIGHT_TO_GRAMS[to_unit]


def convert_temperature(value, from_unit, to_unit):
    """Convert a temperature between Celsius, Fahrenheit, and Kelvin."""
    supported_units = {"C", "F", "K"}

    if from_unit not in supported_units or to_unit not in supported_units:
        raise ValueError("Unsupported temperature unit.")

    # Convert the input to Celsius first.
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero.")

    # Convert Celsius to the requested unit.
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius * 9 / 5 + 32
    else:
        return celsius + 273.15
