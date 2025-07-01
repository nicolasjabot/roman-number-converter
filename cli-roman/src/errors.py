class NumberError(Exception):
    """Base class for Roman-specific issues."""

class RomanFormatError(NumberError):
    """Input string is not a legal Roman numeral """

class ArabicRangeError(NumberError):
    """Arabic integer is outside the supported range."""
