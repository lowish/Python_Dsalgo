# Prince William M. Tan
# WD-202

def selection_sort(arr):
    # Copy the list to keep the original unchanged
    data = arr.copy()
    n = len(data)

    for i in range(n):
        min_idx = i

        # small value
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j

        # Swap values
        data[i], data[min_idx] = data[min_idx], data[i]

    return data


def insertion_sort(arr):
    # Copy the list to keep the original unchanged
    data = arr.copy()

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Move larger values to the right
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        # Insert key into the correct position
        data[j + 1] = key

    return data


def main():
    user_input = input("Enter 10 integers:\n")
    numbers = list(map(int, user_input.split()))

    selection_result = selection_sort(numbers)
    insertion_result = insertion_sort(numbers)

    print("\nSelection Sort Result:")
    print(*selection_result)

    print("\nInsertion Sort Result:")
    print(*insertion_result)


if __name__ == "__main__":
    main()