import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = []

print("Enter elements of the matrix:")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i},{j}): "))
        row.append(element)
    matrix1.append(row)

print("Matrix:")
print(np.array(matrix1))

n = int(input("Enter number for scalar multiplication: "))

scalar = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] * n)
    scalar.append(row)

print("The scalar multiplication is:")
print(np.array(scalar))