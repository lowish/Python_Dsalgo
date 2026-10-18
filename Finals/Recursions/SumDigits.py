def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

num = int(input("Enter a number: "))
print("\n--- Output ---")
print(f"Sum of digits: {sum_digits(abs(num))}")