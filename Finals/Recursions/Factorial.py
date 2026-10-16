def factorial(n):
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

try:
    n = int(input("Enter a non-negative integer: "))
    print("\n--- Output ---")
    print(f"Factorial: {factorial(n)}")
except ValueError as e:
    print(f"Error: {e}")