from roman import roman_to_int_logic, int_to_roman_logic
from errors import RomanFormatError, ArabicRangeError, NumberError, CLIError
import typer
import click
import sys
import logging
from redis_connection import connect_redis
import os

# ------------------------------------------------------------------------------
app = typer.Typer()

r = connect_redis()
REDIS_TTL = int(os.getenv("REDIS_TTL", "86400"))  # time to live in seconds; 24h
CACHE_PREFIX = "roman_cli:"  

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
@app.command("to-int")
def to_int(roman: str = typer.Argument(..., help="Roman numeral")):
    """Convert Roman numeral to integer"""

    #check the cache
    key = f"{CACHE_PREFIX}roman:{roman.upper()}" #prefix roman in key to cache namespacing clearly

    if r:
        cached = r.get(key)
        if cached is not None:
            typer.echo(cached)
            return

    try:
        result = roman_to_int_logic(roman)
        if r:
            r.setex(key, REDIS_TTL, result)
        typer.echo(result)
    except RomanFormatError as exc:
        raise CLIError(str(exc), 2)
    except NumberError as exc:
        raise CLIError(str(exc), 99)


@app.command("to-roman")
def to_roman(number: int = typer.Argument(..., help="> 1")):
    key = f"{CACHE_PREFIX}arabic:{number}"

    if r:
        cached = r.get(key)
        if cached is not None:
            typer.echo(cached)
            return

    try:
        result = int_to_roman_logic(number)
        if r:
            r.setex(key, REDIS_TTL, result)
        typer.echo(result)
    except ArabicRangeError as exc:
        raise CLIError(str(exc), 3)
    except NumberError as exc:
        raise CLIError(str(exc), 99)

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler('roman_cli.log'),
            logging.StreamHandler()
        ],
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    try:
        app()
    except Exception as exc:
        logger.exception("Internal failure: %s", exc)  # This logs the full traceback
        click.echo(f"Internal failure: {exc}", err=True)
        sys.exit(99)
