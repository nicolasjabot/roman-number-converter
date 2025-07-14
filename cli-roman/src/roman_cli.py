from roman import roman_to_int_logic, int_to_roman_logic
from errors import RomanFormatError, ArabicRangeError, NumberError, CLIError
import typer
import click
import sys
import logging
import redis
import os

# ------------------------------------------------------------------------------
# Redis connection
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
REDIS_TTL = int(os.getenv("REDIS_TTL", "86400"))   # seconds; 24 h default

try:
    r = redis.Redis.from_url(REDIS_URL, decode_responses=True)
    r.ping()  # fail fast if the server is unreachable
except redis.exceptions.RedisError as exc:
    r = None  # will fall back to no-cache mode
    print(f"WARNING: Redis unavailable ({exc}); cache disabled", file=sys.stderr)

# ------------------------------------------------------------------------------

logger = logging.getLogger(__name__)
app = typer.Typer()

CACHE_PREFIX = "roman_cli:"  

# ------------------------------------------------------------------------------
#refactor to 
    #check the cache it exists
    #convert and save to cache 
@app.command("to-int")
def to_int(roman: str = typer.Argument(..., help="Roman numeral")):
    """Convert Roman numeral to integer"""

    #check the cache
    key = f"{CACHE_PREFIX}roman:{roman.upper()}"

    try:
        typer.echo(roman_to_int_logic(roman))
    except RomanFormatError as exc:
        raise CLIError(str(exc), 2) from None
    except NumberError as exc:
        raise CLIError(str(exc), 99) from None


@app.command("to-roman")
def to_roman(number: int = typer.Argument(..., help="> 1")):
    try:
        typer.echo(int_to_roman_logic(number))
    except ArabicRangeError as exc:
        raise CLIError(str(exc), 3) from None #remove from none
    except NumberError as exc:
        raise CLIError(str(exc), 99) from None

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,  # Changed to DEBUG for more detail
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
