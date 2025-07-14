# Roman Numeral Converter

## Requirements:
A small command-line application for converting between Roman numerals and Arabic integers.

## Features

- Convert a Roman numeral (e.g. `XIV`) to an integer.
- Convert an integer to its Roman numeral representation.
- Supports numbers equal and greater than 1

## Usage

Install the required dependencies (for example using `pip`):

```bash
pip install typer click
```

Run the CLI using Python:

```bash
python cli-roman/src/roman_cli.py to-int XIV
python cli-roman/src/roman_cli.py to-roman 42
```

Both commands print the converted value on the command line.

## Good to know:

### Logging Strategy

This project uses Python's standard `logging` module. Library code obtains loggers using `logging.getLogger(__name__)` so that applications can configure handlers as needed.

### Testing

Tests are found under cli-roman/tests. The project uses `pytest` library to test the various components of the roman numeral converter.