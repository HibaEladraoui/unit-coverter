import pytest

from unit_converter import (
    convert_length,
    convert_weight,
    convert_temperature,
)


def test_kilometers_to_meters():
    assert convert_length(2, "km", "m") == 2000


def test_unsupported_length_unit():
    with pytest.raises(ValueError):
        convert_length(5, "m", "yard")


def test_kilograms_to_grams():
    assert convert_weight(2, "kg", "g") == 2000


def test_celsius_to_fahrenheit():
    assert convert_temperature(0, "C", "F") == 32


def test_fahrenheit_to_celsius():
    assert convert_temperature(212, "F", "C") == 100


def test_temperature_below_absolute_zero():
    with pytest.raises(ValueError):
        convert_temperature(-300, "C", "K")
