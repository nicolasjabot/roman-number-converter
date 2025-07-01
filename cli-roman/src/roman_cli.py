from roman import roman_to_int_logic, int_to_roman_logic
from errors import RomanFormatError, ArabicRangeError, NumberError
import typer
import click 
app = typer.Typer()

class CLIError(click.ClickException):
    """Wraps a domain error and sets the desired exit code."""
    def __init__(self, msg: str, exit_code: int):
        super().__init__(msg)
        self.exit_code = exit_code


@app.command("to-int")
def to_int(roman: str = typer.Argument(..., help="Roman numeral")):
    """Convert Roman numeral to integer"""
    try:
        typer.echo(roman_to_int_logic(roman))
    except RomanFormatError as exc:
        raise CLIError(str(exc), 2) from None
    except NumberError as exc:            # fallback: future subclasses
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
    except Exception as exc:           # programmer mistake
        click.echo(f"Internal failure: {exc}", err=True)
        sys.exit(99)