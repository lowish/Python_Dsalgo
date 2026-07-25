num_rows = int(input("Enter number of rows: "))

matrix = []


for _ in range(num_rows):
    row_input = input("Enter row values: ")
    row = [int(x) for x in row_input.split()]
    matrix.append(row)


row_index = int(input("Enter row index to modify: "))
value_to_append = int(input("Enter value to append: "))


matrix[row_index].append(value_to_append)


print("\n--- Output ---")
for row in matrix:
    print(row)