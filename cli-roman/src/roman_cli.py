from roman import roman_to_int_logic, int_to_roman_logic
from errors import RomanFormatError, ArabicRangeError, NumberError, CLIError
import typer
import click
import sys


app = typer.Typer()

# ------------------------------------------------------------------------------

@app.command("to-int")
def to_int(roman: str = typer.Argument(..., help="Roman numeral")):
    """Convert Roman numeral to integer"""
    try:
        typer.echo(roman_to_int_logic(roman))
    except RomanFormatError as exc:
        raise CLIError(str(exc), 2) from None
    except NumberError as exc:
        raise CLIError(str(exc), 99) from None


@app.command("to-roman")
def to_roman(number: int = typer.Argument(..., help="1–3999")):
    try:
        typer.echo(int_to_roman_logic(number))
    except ArabicRangeError as exc:
        raise CLIError(str(exc), 3) from None
    except NumberError as exc:
        raise CLIError(str(exc), 99) from None

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        app()
    except Exception as exc:
        click.echo(f"Internal failure: {exc}", err=True)
        sys.exit(99)