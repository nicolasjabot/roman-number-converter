# Roman Numeral Converter

## Requirements:
A small command-line application for converting between Roman numerals and Arabic integers.

## Features

- Convert a Roman numeral (e.g. `XIV`) to an integer.
- Convert an integer to its Roman numeral representation.
- Supports numbers equal and greater than 1

## Usage

### Option 1: 

- Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

- Install the required package to run the cli (for example using `pip`):

```bash
pip install -e .
```

Run the CLI using Python:

```bash
python roman to-int XIV
python roman to-roman 42
```

Both commands print the converted value on the command line.

### Option 2: Docker 

Build the Docker image:
```bash
docker build -t roman-converter .
```

Run the converter using Docker:
```bash
docker run roman-converter roman to-int XIV
docker run roman-converter roman to-roman 42
```
The commands will output the converted values directly to the console, just like the local Python installation.

Note: The Docker approach doesn't require Python installation on your local machine and should ensure consistent 
execution across different environments.


## Good to know:

### Caching 
The application uses Redis for caching conversion results:

- Redis server must be running locally or accessible via network
- Default connection: `redis://localhost:6379`

When using Docker, you can link the converter to a Redis container:
```bash
# Start Redis container
docker run -d --name redis-cache redis
```

### Logging Strategy

This project uses Python's standard `logging` module. Library code obtains loggers using `logging.getLogger(__name__)` so that applications can configure handlers as needed.
Logs will be visible under src/roman_cli.log 

### Testing

Unit tests are found under cli-roman/tests. The project uses `pytest` library to test the various components of the roman numeral converter.