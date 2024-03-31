
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print("Matrix:")
for row in matrix:
  print(row)


row_index = 1  # Row index (0-based)
col_index = 2  # Column index (0-based)
element = matrix[row_index][col_index]
print("Element at row", row_index + 1, "column", col_index + 1, ":", element)
