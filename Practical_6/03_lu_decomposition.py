# Apply LU Decomposition for Linear Systems
import numpy as np

# User Input
n = int(input("Enter order of square matrix A (n): "))
print(f"Enter {n}x{n} coefficient matrix A row by row:")
A_rows = []
for i in range(n):
    A_rows.append(list(map(float, input(f"Row {i + 1}: ").split())))
A = np.array(A_rows, dtype=float)

B = np.array(list(map(float, input(f"Enter {n} constants for vector B (space-separated): ").split())), dtype=float)

L = np.zeros((n, n))
U = np.zeros((n, n))

# Step 1: Perform LU Decomposition (Doolittle's method)
for i in range(n):
    # Upper Triangular
    for k in range(i, n):
        sum_ = sum(L[i][j] * U[j][k] for j in range(i))
        U[i][k] = A[i][k] - sum_
    # Lower Triangular
    L[i][i] = 1
    for k in range(i + 1, n):
        sum_ = sum(L[k][j] * U[j][i] for j in range(i))
        L[k][i] = (A[k][i] - sum_) / U[i][i]

print("L (Lower Triangular Matrix):\n", L)
print("\nU (Upper Triangular Matrix):\n", U)

# Step 2: Solve L * y = B (Forward substitution)
y = np.zeros(n)
for i in range(n):
    y[i] = B[i] - sum(L[i][j] * y[j] for j in range(i))

# Step 3: Solve U * x = y (Backward substitution)
x = np.zeros(n)
for i in reversed(range(n)):
    x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

print("\nSolution: x =", x)


"""

================================================================================
THEORY: LU DECOMPOSITION (DOOLITTLE'S METHOD)
================================================================================

1. AIM OF THE MATH CONCEPT:
   To factorize matrix A into L * U and solve A * x = B efficiently via forward
   and backward substitution.

2. FORMULA:
   A = L * U
   L * y = B  (Forward Substitution)
   U * x = y  (Backward Substitution)

3. TERMS OF FORMULA:
   - L : Lower triangular matrix with 1s on diagonal.
   - U : Upper triangular matrix.
   - y : Intermediate vector.
   - x : Solution vector.

4. DEFINITION:
   LU Decomposition expresses a square matrix as the product of a lower and an
   upper triangular matrix.

5. THEORY RELATED:
   Once factored, solving for multiple B vectors takes only O(n^2) time.

6. REAL-LIFE APPLICATIONS:
   - Finite element solvers, circuit simulation (SPICE), matrix inversion.

7. EXAMPLES:
   A = [[2, 3, 1], [4, 7, 5], [6, 18, 19]], B = [1, 2, 3] -> x = [0.5, 0, 0].

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Solve A = [[2, 3], [4, 7]], B = [1, 2]:
   Step 1: Doolittle's LU:
       U[0] = [2, 3],  L[1][0] = 4/2 = 2,  U[1][1] = 7 - 2*3 = 1.
       L = [[1, 0], [2, 1]],  U = [[2, 3], [0, 1]].
   Step 2: Forward Substitution (L*y = B):
       y1 = 1,  2*y1 + y2 = 2 => y2 = 0.
   Step 3: Backward Substitution (U*x = y):
       1*x2 = 0 => x2 = 0,  2*x1 + 3*x2 = 1 => x1 = 0.5.
   Final Answer: x = [0.5, 0.0].
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 2
# 2 3
# 4 7
# 1 2
