def non_negative_integer(func):
    def wrapper(n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Argument must be a non-negative integer")
        return func(n)
    return wrapper

@non_negative_integer
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
try:
    print(factorial(7))  # Output: 120
    print(factorial(-15)) # Raises ValueError
except ValueError as e:
    print(e)
