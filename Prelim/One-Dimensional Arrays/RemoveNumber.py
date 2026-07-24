numbers_input = input("Enter numbers: ")


numbers = [int(x) for x in numbers_input.split()]


to_remove = int(input("Enter the value to remove: "))


updated_numbers = [num for num in numbers if num != to_remove]


print("\n--- Output ---")
print(updated_numbers)