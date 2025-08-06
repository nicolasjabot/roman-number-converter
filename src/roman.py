import sys
import logging
from errors import RomanFormatError, ArabicRangeError, NumberError


logger = logging.getLogger(__name__)

# constants---------------------------------------------------------------------
# reafctor as enum?
ROMAN_DIGITS = {
    'I': 1,   'V': 5,
    'X': 10,  'L': 50,
    'C': 100, 'D': 500,
    'M': 1000
}

ARABIC_TO_ROMAN = (
    (1000, 'M'), (900, 'CM'),
    (500,  'D'), (400, 'CD'),
    (100,  'C'), (90,  'XC'),
    (50,   'L'), (40,  'XL'),
    (10,   'X'), (9,   'IX'),
    (5,    'V'), (4,   'IV'),
    (1,    'I')
)
# ------------------------------------------------------------------------------

def roman_to_int_logic(roman: str) -> int:
    # logger.debug("Starting conversion of Roman numeral: %s", roman)
    if not isinstance(roman, str):
        logger.error("Invalid input type: %s", type(roman).__name__)
        raise TypeError("roman must be str")
    if not roman:
        logger.error("Empty string provided")
        raise RomanFormatError("empty string")

    total, prev = 0, 0
    for ch in reversed(roman.upper()):
        try:
            val = ROMAN_DIGITS[ch]
        except KeyError:
            raise RomanFormatError(f"invalid digit: {ch}") from None
        total = total - val if val < prev else total + val
        prev = max(prev, val)

    if int_to_roman_logic(total) != roman.upper():
        logger.error("Invalid Roman numeral format: %s", roman)
        raise RomanFormatError(f"invalid format {roman!r}")
    # logger.debug("Successfully converted %s to %d", roman, total)
    return total


def int_to_roman_logic(n: int) -> str:
    # logger.debug("Starting conversion of %d to Roman numeral", n)
    if not isinstance(n, int) or isinstance(n, bool):
        logger.error("Invalid input type: %s", type(n).__name__)
        raise TypeError("number must be int (not bool)")
    if not 1 <= n:
        logger.error("Number %d out of valid range, greater than 0", n)
        raise ArabicRangeError("number must be greater than 1")

    out = []
    for val, sym in ARABIC_TO_ROMAN:
        count, n = divmod(n, val)
        out.append(sym * count)
    result = ''.join(out)
    # logger.debug("Successfully converted %d to %s", n, result)
    return result
