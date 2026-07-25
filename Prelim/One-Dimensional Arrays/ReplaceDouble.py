numbers_input = input("Enter numbers: ")

numbers = [int(x) for x in numbers_input.split()]

index = int(input("Enter the index to double: "))

numbers[index] *= 2

print("\n--- Output ---")
print(numbers)