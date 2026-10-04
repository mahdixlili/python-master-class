print(
    "Please enter a 3x3 matrix (one row per line, separated by spaces):"
    "\nExample:"
    "\n1 2 3"
    "\n4 5 6"
    "\n7 8 9"
    "\n"
)

matrix = []
for i in range(1, 4):
    row = [int(x) for x in input(f"Row {i}: ").split()]
    matrix.append(row)

print("\nRow sums:")
for i, row in enumerate(matrix, start=1):
    print(f"Row {i}: {sum(row)}")

print("\nColumn sums:")
for j in range(3):
    col_total = matrix[0][j] + matrix[1][j] + matrix[2][j]
    print(f"Column {j + 1}: {col_total}")
