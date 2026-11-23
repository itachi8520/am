# Diagonalization of matrix
import math

def multiply_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_val = 0
            for k in range(len(B)):
                sum_val += A[i][k] * B[k][j]
            row.append(sum_val)
        result.append(row)
    return result

def inverse_2x2(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        print("Matrix is singular and cannot be inverted")
        return None
    return [
        [matrix[1][1] / det, -matrix[0][1] / det],
        [-matrix[1][0] / det, matrix[0][0] / det]
    ]

def compute_eigen_2x2(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    # Characteristic Equation: lambda^2 - (a + d)lambda + (ad - bc) = 0
    trace = a + d
    determinant = a * d - b * c
    discriminant = trace ** 2 - 4 * determinant
    if discriminant < 0:
        print("Complex eigenvalues, not supported here.")
        return None, None
    sqrt_disc = math.sqrt(discriminant)
    lambda1 = (trace + sqrt_disc) / 2
    lambda2 = (trace - sqrt_disc) / 2

    # Find eigenvectors manually (one for each eigenvalue)
    def find_vector(lam):
        # (A - lambda*I)v = 0 => Solve: (a - lam)v1 + b*v2 = 0
        # Choose v2 = 1
        v1 = -(b) / (a - lam) if (a - lam) != 0 else 1
        return [v1, 1]

    eigenvector1 = find_vector(lambda1)
    eigenvector2 = find_vector(lambda2)
    return [lambda1, lambda2], [eigenvector1, eigenvector2]

# User Input
print("Enter elements of 2x2 matrix A row by row (2 space-separated numbers per row):")
row1 = list(map(float, input("Row 1: ").split()))
row2 = list(map(float, input("Row 2: ").split()))
A = [row1, row2]

eigenvalues, eigenvectors = compute_eigen_2x2(A)
if eigenvalues is not None:
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:", eigenvectors)
    P = [
        [eigenvectors[0][0], eigenvectors[1][0]],
        [eigenvectors[0][1], eigenvectors[1][1]]
    ]
    print("Matrix P:", P)
    P_inv = inverse_2x2(P)
    print(P_inv)
    if P_inv is not None:
        D = multiply_matrices(P_inv, multiply_matrices(A, P))
        print(D)


"""

================================================================================
THEORY: DIAGONALIZATION OF A MATRIX
================================================================================

1. AIM OF THE MATH CONCEPT:
   To express a square matrix A in diagonal form D = P^(-1) * A * P using its
   eigenvalues and eigenvectors.

2. FORMULA:
   - Characteristic Equation: det(A - lambda * I) = 0
     For 2x2: lambda^2 - trace(A)*lambda + det(A) = 0
   - Eigenvector Equation: (A - lambda * I) * v = 0
   - Diagonalization: D = P^(-1) * A * P

3. TERMS OF FORMULA:
   - A      : Square matrix of order n x n.
   - lambda : Eigenvalues of A.
   - v      : Non-zero eigenvectors corresponding to lambda.
   - P      : Modal matrix whose columns are the eigenvectors of A.
   - D      : Diagonal matrix with eigenvalues on the main diagonal.

4. DEFINITION:
   A square matrix A is diagonalizable if there exists an invertible matrix P
   such that P^(-1) * A * P = D is a diagonal matrix.

5. THEORY RELATED:
   An n x n matrix is diagonalizable if and only if it has n linearly independent
   eigenvectors. Diagonalization makes computing powers of A fast since
   A^k = P * D^k * P^(-1).

6. REAL-LIFE APPLICATIONS:
   - Principal Component Analysis (PCA) in machine learning.
   - Vibration analysis in mechanical engineering.
   - Solving systems of linear differential equations.
   - Quantum mechanics (energy eigenstates).

7. EXAMPLES:
   Diagonalizing A = [[4, 1], [2, 3]] gives eigenvalues 5 and 2, and D = [[5, 0], [0, 2]].

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Diagonalize A = [[4, 1], [2, 3]].

   Step 1: Find Eigenvalues:
       trace = 4 + 3 = 7,  det = (4)(3) - (1)(2) = 10
       lambda^2 - 7*lambda + 10 = 0  =>  (lambda - 5)(lambda - 2) = 0
       lambda1 = 5,  lambda2 = 2.

   Step 2: Find Eigenvectors:
       For lambda1 = 5: (4 - 5)v1 + 1*v2 = 0 => -v1 + v2 = 0 => v1 = [1, 1]^T
       For lambda2 = 2: (4 - 2)v1 + 1*v2 = 0 => 2v1 + v2 = 0 => v2 = [-0.5, 1]^T

   Step 3: Form Modal Matrix P and its Inverse P^(-1):
       P = [[1, -0.5], [1, 1]],   det(P) = 1 - (-0.5) = 1.5
       P^(-1) = (1 / 1.5) * [[1, 0.5], [-1, 1]]

   Step 4: Compute D = P^(-1) * A * P:
       A * P = [[5, -1], [5, 2]]
       D = P^(-1) * (A * P) = [[5, 0], [0, 2]].
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 4 1
# 2 3
