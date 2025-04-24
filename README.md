# Factorial Calculator

A simple Python program that calculates the factorial of a number using recursion.

## Description

This program provides a function to calculate the factorial of a non-negative integer. The factorial of a number n (written as n!) is the product of all positive integers less than or equal to n.

For example:
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 0! = 1 (by definition)

## Usage

```python
from factorial import factorial

# Calculate factorial of 5
result = factorial(5)
print(result)  # Output: 120
```

## Features

- Calculates factorial using recursive approach
- Includes input validation for negative numbers
- Simple and easy to use
- Includes docstring documentation

## Error Handling

The function includes error handling for:
- Negative numbers (raises ValueError)

## Requirements

- Python 3.x

## License

This project is open source and available under the MIT License.