# Number Processor

A non-interactive Python script for numeric data processing with advanced statistical functions and reusable components.

## Features

- **Data Sanitization**: Clean and validate numeric input from various sources
- **Statistical Analysis**: Moving averages, min/max/mean calculations
- **Data Normalization**: Scale values to [0,1] range
- **Modular Design**: Reusable `DataProcessor` class and utility functions
- **Command-Line Interface**: Easy-to-use CLI with flexible input options
- **Comprehensive Testing**: Unit tests for all components

## Project Structure

```
test-sample-python/
├── app/
│   ├── main.py          # CLI entry point and argument parsing
│   └── processing.py    # Core DataProcessor class and utilities
├── tests/
│   ├── test_main.py     # Tests for CLI functionality
│   └── test_processing.py  # Tests for processing functions
├── pyproject.toml       # Project configuration and dependencies
└── README.md           # This file
```

## Installation

1. **Clone or download the project**
2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install the package**:
   ```bash
   pip install -e .
   ```

## Usage

### Command Line Interface

The script can be run in several ways:

#### Basic Usage

```bash
# Direct Python execution
python -m app.main 1 2 3 4 5

# Using the installed script (after pip install -e .)
number-processor 1 2 3 4 5
```

#### Advanced Options

```bash
# With moving average window
python -m app.main 1 2 3 4 5 --window 3

# With normalization to [0,1] range
python -m app.main 1 2 3 4 5 --normalize

# Mixed input formats (comma-separated and space-separated)
python -m app.main "1,2,3" 4 5 --window 2

# Help
python -m app.main --help
```

### Programmatic Usage

```python
from app.processing import DataProcessor, sanitize_numbers

# Create processor from raw data
raw_data = ["1", 2, 3.5, None, "4.5"]
processor = DataProcessor.from_raw(raw_data)

# Apply transformations
normalized = processor.normalize_0_1()
smoothed = normalized.with_moving_average(window_size=3)

# Get statistics
min_val, mean_val, max_val = smoothed.summary()
print(f"Min: {min_val}, Mean: {mean_val}, Max: {max_val}")
```

## API Reference

### Core Functions

#### `sanitize_numbers(values: Iterable[object]) -> List[float]`

- Cleans and validates numeric input
- Handles strings, numbers, None values
- Raises `ValueError` for invalid inputs

#### `moving_average(values: Sequence[float], window_size: int) -> List[float]`

- Computes simple moving average
- Uses prefix averaging for initial values

#### `summarize(values: Sequence[float]) -> Tuple[Optional[float], Optional[float], Optional[float]]`

- Returns (min, mean, max) tuple
- Returns (None, None, None) for empty sequences

### DataProcessor Class

#### `DataProcessor(values: List[float])`

- Main processing class for numeric data

#### Methods:

- `from_raw(raw_values)` - Create from mixed input types
- `normalize_0_1()` - Normalize to [0,1] range
- `with_moving_average(window_size)` - Apply moving average
- `summary()` - Get min/mean/max statistics

## Command Line Options

| Option        | Description                                 | Default |
| ------------- | ------------------------------------------- | ------- |
| `numbers`     | Space or comma-separated numbers to process | None    |
| `--window`    | Moving average window size                  | 3       |
| `--normalize` | Normalize values to [0,1] range             | False   |
| `--help`      | Show help message                           | -       |

## Examples

### Example 1: Basic Processing

```bash
$ python -m app.main 1 2 3 4 5
count=5 min=1.0 mean=3.0 max=5.0 values=[1.0, 1.5, 2.0, 3.0, 4.0]
```

### Example 2: With Normalization

```bash
$ python -m app.main 10 20 30 40 --normalize
count=4 min=0.0 mean=0.5 max=1.0 values=[0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
```

### Example 3: Custom Window Size

```bash
$ python -m app.main 1 2 3 4 5 6 --window 2
count=6 min=1.0 mean=3.5 max=6.0 values=[1.0, 1.5, 2.5, 3.5, 4.5, 5.5]
```

## Testing

Run the test suite:

```bash
# Using pytest (recommended)
pytest

# Using unittest
python -m unittest discover tests
```

Test coverage includes:

- Data sanitization edge cases
- Moving average calculations
- Normalization functions
- CLI argument parsing
- End-to-end pipeline execution

## Development

### Adding New Features

1. **Processing Functions**: Add to `app/processing.py`
2. **CLI Options**: Update `parse_args()` in `app/main.py`
3. **Tests**: Add corresponding tests in `tests/`

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Add docstrings for public functions
- Write tests for new functionality

## Requirements

- Python 3.8+
- No external dependencies (uses only standard library)

## License

This project is open source. Feel free to use and modify as needed.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Troubleshooting

### Common Issues

**"Cannot parse number from string"**

- Ensure all inputs are valid numbers
- Check for empty strings or non-numeric characters

**"window_size must be positive"**

- Use positive integers for the `--window` option

**Import errors**

- Make sure you're in the project directory
- Activate your virtual environment
- Install the package with `pip install -e .`

### Getting Help

- Check the help: `python -m app.main --help`
- Review the examples above
- Check the test files for usage patterns
