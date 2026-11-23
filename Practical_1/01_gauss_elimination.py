# Gauss Elimination
import numpy as np
import sys

def gauss_elimination(A):
    n = A.shape[0]  # Number of unknowns (and rows)
    # Elimination Phase
    for i in range(n):
        # Find pivot element (largest absolute value in the current column below the diagonal)
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k, i]) > abs(A[max_row, i]):
                max_row = k
        # Swap rows to bring the pivot to the current diagonal position
        A[[i, max_row]] = A[[max_row, i]]
        # Check for division by zero (singular matrix)
        if A[i, i] == 0:
            print("Divide by zero detected or singular matrix. No unique solution exists.")
            return None
        # Eliminate elements below the current pivot
        for k in range(i + 1, n):
            factor = A[k, i] / A[i, i]
            A[k, i:] = A[k, i:] - factor * A[i, i:]

    # Backward Substitution Phase
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if A[i, i] == 0:  # Check for zero on diagonal during back substitution
            print("Singular matrix detected during back substitution. No unique solution exists.")
            return None
        X[i] = A[i, n] / A[i, i]
        for k in range(i - 1, -1, -1):
            A[k, n] = A[k, n] - A[k, i] * X[i]
    return X

# User Input
n = int(input("Enter number of unknowns/equations (n): "))
print(f"Enter the augmented matrix [A | B] row by row ({n + 1} space-separated values per row):")
rows = []
for i in range(n):
    rows.append(list(map(float, input(f"Row {i + 1}: ").split())))
augmented_matrix = np.array(rows, dtype=float)

print("Original Augmented Matrix:")
print(augmented_matrix)

solution = gauss_elimination(augmented_matrix.copy())  # Use .copy() to avoid modifying original
if solution is not None:
    print("\nSolution:")
    print(solution)


"""

================================================================================
THEORY: GAUSS ELIMINATION METHOD
================================================================================

1. AIM OF THE MATH CONCEPT:
   To solve a system of 'n' linear equations in 'n' unknowns by reducing the
   augmented matrix to upper triangular form and finding unknowns via backward
   substitution.

2. FORMULA:
   System: A * X = B   |   Augmented Matrix: [A | B]
   Elimination: R_k -> R_k - (a_ki / a_ii) * R_i   (for k > i)
   Backward Substitution: x_i = (b_i' - sum(a_ij' * x_j for j = i+1..n)) / a_ii'

3. TERMS OF FORMULA:
   - A       : n x n coefficient matrix.
   - X       : n x 1 vector of unknowns [x1, x2, ..., xn]^T.
   - B       : n x 1 constant vector.
   - a_ii    : Pivot element on the diagonal.
   - factor  : Multiplier (a_ki / a_ii) used to zero out elements below pivot.

4. DEFINITION:
   Gauss Elimination is a direct numerical method in linear algebra that uses
   elementary row operations to convert a linear system into an equivalent upper
   triangular system.

5. THEORY RELATED:
   Elementary row operations preserve the solution set of the system. Partial
   pivoting swaps rows so the largest absolute value in the column becomes the
   pivot, preventing division by zero and minimizing round-off errors.

6. REAL-LIFE APPLICATIONS:
   - Electrical circuit analysis (Kirchhoff's laws).
   - Structural engineering (finite element analysis).
   - Economics (input-output production models).
   - Computer graphics (3D transformations).

7. EXAMPLES:
   Solving 3x3 linear systems like x + 2y + 3z = 10, x + 3y + 4z = 40, x + y + z = 40.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Solve:
       x + 2y + 3z = 10   (R1)
       x + 3y + 4z = 40   (R2)
       x +  y +  z = 40   (R3)

   Step 1: Write Augmented Matrix [A | B]:
       [ 1  2  3 | 10 ]
       [ 1  3  4 | 40 ]
       [ 1  1  1 | 40 ]

   Step 2: Eliminate column 1 below R1 (R2 -> R2 - R1, R3 -> R3 - R1):
       [ 1   2   3 | 10 ]
       [ 0   1   1 | 30 ]
       [ 0  -1  -2 | 30 ]

   Step 3: Eliminate column 2 below R2 (R3 -> R3 + R2):
       [ 1   2   3 | 10 ]
       [ 0   1   1 | 30 ]
       [ 0   0  -1 | 60 ]

   Step 4: Backward Substitution:
       From R3: -z = 60  =>  z = -60
       From R2: y + (-60) = 30  =>  y = 90
       From R1: x + 2(90) + 3(-60) = 10  =>  x + 180 - 180 = 10  =>  x = 10
   Final Answer: x = 10, y = 90, z = -60.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 3
# 1 2 3 10
# 1 3 4 40
# 1 1 1 40
