num_rows = int(input("Enter number of rows: "))

matrix = []


for _ in range(num_rows):
    row_input = input("Enter row values: ")
    row = [int(x) for x in row_input.split()]
    matrix.append(row)

row_index = int(input("Enter row index: "))
column_index = int(input("Enter column index: "))


print("\n--- Output ---")
print(f"Element: {matrix[row_index][column_index]}")