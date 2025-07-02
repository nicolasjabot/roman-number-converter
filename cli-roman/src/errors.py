import click 

class NumberError(Exception):
    """Base class for Roman-specific issues."""

class RomanFormatError(NumberError):
    """Input string is not a legal Roman numeral """

class ArabicRangeError(NumberError):
    """Arabic integer is outside the supported range."""

class CLIError(click.ClickException):
    """Wraps a domain error and sets the desired exit code."""
    def __init__(self, msg: str, exit_code: int):
        super().__init__(msg)
        self.exit_code = exit_code