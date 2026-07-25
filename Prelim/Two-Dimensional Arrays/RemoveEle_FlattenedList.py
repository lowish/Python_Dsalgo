num_rows = int(input("Enter number of rows: "))

matrix = []

for _ in range(num_rows):
    row_input = input("Enter row values: ")
    row = [int(x) for x in row_input.split()]
    matrix.append(row)


row_index = int(input("Enter row index to remove from: "))
column_index = int(input("Enter column index to remove: "))


matrix[row_index].pop(column_index)


flattened_list = []
for row in matrix:
    for element in row:
        flattened_list.append(element)


print("\n--- Output ---")
print(flattened_list)