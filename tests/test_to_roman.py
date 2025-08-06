import pytest
from roman import int_to_roman_logic
from errors import ArabicRangeError

@pytest.mark.parametrize("key, expected", [
    (2, "II"),
    (3, "III"),
    (4000, "MMMM"),
    (2023, "MMXXIII"),
    (3999, "MMMCMXCIX"),
    (2444, "MMCDXLIV"),
    (55, "LV"),
    (99, "XCIX"),
    (101, "CI")
])

def test_roman_conversions(key, expected):
    assert int_to_roman_logic(key) == expected

@pytest.mark.parametrize("invalid_type", [
    True, #test boolean output
    1.5, #test float output
    "1" #test string output
])

def test_type_errors(invalid_type):
    with pytest.raises(TypeError):
        int_to_roman_logic(invalid_type)


@pytest.mark.parametrize("invalid_number", [
    0, #test zero input
    -1, #test negative input
])

def test_type_errors(invalid_number):
    with pytest.raises(ArabicRangeError):
        int_to_roman_logic(invalid_number)