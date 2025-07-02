import pytest
from roman import roman_to_int_logic
from errors import RomanFormatError

@pytest.mark.parametrize("key, expected", [
    ("II", 2),
    ("III", 3),
    ("MMMM", 4000),
    ("MMXXIII", 2023),
    ("MMMCMXCIX", 3999),
    ("MMCDXLVI", 2446),
    ("LV", 55),
    ("XCIX", 99),
    ("CI", 101)
])

def test_int_conversion(key, expected):
    assert roman_to_int_logic(key) == expected

@pytest.mark.parametrize("invalid_type", [
    True, #test boolean output
    1.5, #test float output
    1 #test int output
])

def test_type_errors(invalid_type):
    with pytest.raises(TypeError):
        roman_to_int_logic(invalid_type)

@pytest.mark.parametrize("invalid_letter", [
    "A", "B", "E", "F", "G", "H", "J", 
    "K", "N", "O", "P", "Q", "R", 
    "S", "T", "U", "W", "Y", "Z"
])

def test_type_errors(invalid_letter):
    with pytest.raises(RomanFormatError):
        roman_to_int_logic(invalid_letter)