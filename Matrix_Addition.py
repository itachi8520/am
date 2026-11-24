import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix1 = []
matrix2 = []

print("Enter elements for the first matrix:")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i},{j}): "))
        row.append(element)
    matrix1.append(row)

print("First matrix:")
print(matrix1)

print("Enter elements for the second matrix:")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i},{j}): "))
        row.append(element)
    matrix2.append(row)

print("Second matrix:")
print(matrix2)

sum_matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    sum_matrix.append(row)

print("The sum of the matrices is:")
print(np.array(sum_matrix))