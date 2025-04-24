from typing import List, Union
import sys

def factorial(n: int) -> int:
    """
    Calculate the factorial of a given number using recursion.
    
    Args:
        n (int): A non-negative integer
    
    Returns:
        int: The factorial of n
    
    Raises:
        ValueError: If n is negative or not an integer
        RecursionError: If input is too large causing stack overflow
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        try:
            return n * factorial(n - 1)
        except RecursionError:
            raise RecursionError("Input too large for recursive calculation. Use factorial_iterative instead.")

def factorial_iterative(n: int) -> int:
    """
    Calculate the factorial of a given number using iteration.
    More efficient for large numbers as it doesn't use recursion.
    
    Args:
        n (int): A non-negative integer
    
    Returns:
        int: The factorial of n
    
    Raises:
        ValueError: If n is negative or not an integer
        OverflowError: If result exceeds system's maximum integer size
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(1, n + 1):
        # Check for potential overflow
        if result > sys.maxsize // i:
            raise OverflowError(f"Factorial of {n} is too large for this system")
        result *= i
    return result

def fibonacci(n: int) -> List[int]:
    """
    Generate the Fibonacci sequence up to the nth number.
    
    Args:
        n (int): A positive integer representing how many Fibonacci numbers to generate
    
    Returns:
        list: A list containing the Fibonacci sequence up to the nth number
    
    Raises:
        ValueError: If n is negative or not an integer
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    sequence = []
    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)
    
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence

# Example usage
if __name__ == "__main__":
    try:
        # Factorial examples
        number = 5
        # Try both implementations
        result_recursive = factorial(number)
        result_iterative = factorial_iterative(number)
        print(f"The factorial of {number} (recursive) is {result_recursive}")
        print(f"The factorial of {number} (iterative) is {result_iterative}")
        
        # Test large number with iterative version
        large_number = 20
        result_large = factorial_iterative(large_number)
        print(f"\nThe factorial of {large_number} is {result_large}")
        
        # Try to cause RecursionError to demonstrate error handling
        try:
            very_large = 2000
            factorial(very_large)
        except RecursionError as e:
            print(f"\nExpected error for large input: {e}")
            # Show that iterative version still works
            print(f"But iterative version can handle it: {factorial_iterative(very_large)}")
        
        # Fibonacci example
        n = 10
        fib_sequence = fibonacci(n)
        print(f"\nFibonacci sequence up to {n} numbers: {fib_sequence}")
        
    except (ValueError, OverflowError, RecursionError) as e:
        print(f"Error: {e}")