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