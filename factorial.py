def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): A non-negative integer
    
    Returns:
        int: The factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
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
        # Factorial example
        number = 5
        result = factorial(number)
        print(f"The factorial of {number} is {result}")
        
        # Fibonacci example
        n = 10
        fib_sequence = fibonacci(n)
        print(f"\nFibonacci sequence up to {n} numbers: {fib_sequence}")
    except ValueError as e:
        print(f"Error: {e}")