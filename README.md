# Python Math Utilities

A collection of mathematical utility functions implemented in Python, including factorial calculation (both recursive and iterative) and Fibonacci sequence generation.

## Features

### Factorial Calculator
- Two implementations:
  - Recursive approach (memory-efficient for small numbers)
  - Iterative approach (efficient for large numbers)
- Comprehensive error handling
- Type checking and validation
- Overflow protection

### Fibonacci Sequence Generator
- Generates Fibonacci sequence up to nth number
- Input validation
- Type checking

## Usage

### Factorial Calculation
```python
from factorial import factorial, factorial_iterative

# For small numbers, both implementations work well
number = 5
result_recursive = factorial(number)      # Using recursive version
result_iterative = factorial_iterative(number)  # Using iterative version

# For large numbers, use the iterative version
large_number = 1000
result = factorial_iterative(large_number)  # More efficient for large numbers
```

### Fibonacci Sequence
```python
from factorial import fibonacci

# Generate first 10 Fibonacci numbers
n = 10
fib_sequence = fibonacci(n)
print(fib_sequence)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Error Handling

The functions include comprehensive error handling for:
- Negative numbers
- Non-integer inputs
- Stack overflow (for recursive factorial)
- Integer overflow

## Requirements

- Python 3.x

## License

This project is open source and available under the MIT License.