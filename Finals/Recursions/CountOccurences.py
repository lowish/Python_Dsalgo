def count_occurrences(arr, target, index=0):
    if index >= len(arr):
        return 0

    count = 1 if arr[index] == target else 0
    return count + count_occurrences(arr, target, index + 1)


numbers_input = input("Enter numbers: ")
target = int(input("Enter target value: "))

numbers = [int(x) for x in numbers_input.split()]

occurrences = count_occurrences(numbers, target)

print("\n--- Output ---")
print(f"Occurrences: {occurrences}")