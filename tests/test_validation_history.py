import pytest
from validation import validate_value, validate_unit, validate_temperature
from history import ConversionHistory


def test_validate_value_accepts_number():
    assert validate_value(5) == 5.0


def test_validate_unit_accepts_supported_unit():
    assert validate_unit("length", "km") == "km"


def test_temperature_at_absolute_zero_is_allowed():
    assert validate_temperature(-273.15, "C") == -273.15


def test_temperature_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        validate_temperature(-300, "C")


def test_unsupported_unit_raises():
    with pytest.raises(ValueError):
        validate_unit("weight", "banana")


def test_text_value_raises():
    with pytest.raises(TypeError):
        validate_value("abc")


def test_history_stores_and_returns_last():
    h = ConversionHistory()
    h.add(1, "km", "m", 1000)
    assert h.last(1)[0]["result"] == 1000


def test_history_drops_oldest_when_full():
    h = ConversionHistory(max_size=2)
    h.add(1, "m", "cm", 100)
    h.add(2, "m", "cm", 200)
    h.add(3, "m", "cm", 300)
    assert len(h) == 2
    assert h.last(2)[0]["value"] == 2