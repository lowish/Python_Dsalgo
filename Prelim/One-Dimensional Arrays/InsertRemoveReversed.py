numbers_input = input("Enter numbers: ")

numbers = [int(x) for x in numbers_input.split()]

to_insert = int(input("Value to insert at start: "))
numbers.insert(0, to_insert)

to_remove = int(input("Value to remove (first occurrence): "))

if to_remove in numbers:
    numbers.remove(to_remove)

reversed_numbers = numbers[::-1]

print("\n--- Output ---")
print(reversed_numbers)