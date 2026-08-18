
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
  
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

scores = []
for i in range(1, 6):
    score = int(input(f"Enter score {i}: "))
    scores.append(score)

print() 


print(f"Original List: {scores}")
bubble_result = bubble_sort(scores)
print(f"Bubble Sort: {bubble_result}")
selection_result = selection_sort(scores)
print(f"Selection Sort: {selection_result}")