import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

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

result = []

for i in range(rows):
    row = []
    for j in range(cols):
        total = 0
        for k in range(cols):
            total += matrix1[i][k] * matrix2[k][j]
        row.append(total)
    result.append(row)

print("The product of the matrices is:")
print(np.array(result))