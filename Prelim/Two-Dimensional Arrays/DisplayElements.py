num_rows = int(input("Enter number of rows: "))

matrix = []

for _ in range(num_rows):
    row_input = input("Enter row values: ")
    row = [int(x) for x in row_input.split()]
    matrix.append(row)

print("\n--- Output ---")
for row in matrix:
    print(row)