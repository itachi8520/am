# Lagrange Interpolation Formula
def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

# User Input data points
x_values = list(map(float, input("Enter x_values (space-separated): ").split()))
y_values = list(map(float, input("Enter y_values (space-separated): ").split()))

# Value to estimate
x_to_find = float(input("Enter value of x to estimate: "))

# Apply Lagrange Interpolation
y_estimated = lagrange_interpolation(x_values, y_values, x_to_find)
print(f"Estimated value of f({x_to_find}) = {y_estimated:.2f}")


"""

================================================================================
THEORY: LAGRANGE INTERPOLATION FORMULA
================================================================================

1. AIM OF THE MATH CONCEPT:
   To estimate f(x) at an intermediate point x from given data points (x_i, y_i)
   that may be unequally spaced.

2. FORMULA:
   P(x) = sum_{i=0}^{n-1} y_i * product_{j!=i} ((x - x_j) / (x_i - x_j))

3. TERMS OF FORMULA:
   - (x_i, y_i) : Known data points.
   - x          : Target point for estimation.
   - P(x)       : Interpolating polynomial of degree <= n - 1.

4. DEFINITION:
   Lagrange Interpolation constructs a unique polynomial passing through all
   given points without needing equal intervals between x-values.

5. THEORY RELATED:
   Works for both equally and unequally spaced data.

6. REAL-LIFE APPLICATIONS:
   - Signal reconstruction, computer graphics, Shamir's Secret Sharing.

7. EXAMPLES:
   x_values = [5, 7, 11, 13], y_values = [150, 392, 1452, 2366], x = 10.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Given points (1, 1), (2, 4), (4, 16), estimate f(3):
   Step 1: Term 0 (i=0): 1 * ((3-2)/(1-2)) * ((3-4)/(1-4)) = 1 * (-1) * (1/3) = -1/3.
   Step 2: Term 1 (i=1): 4 * ((3-1)/(2-1)) * ((3-4)/(2-4)) = 4 * (2) * (1/2) = 4.
   Step 3: Term 2 (i=2): 16 * ((3-1)/(4-1)) * ((3-2)/(4-2)) = 16 * (2/3) * (1/2) = 16/3.
   Step 4: Sum = -1/3 + 4 + 16/3 = 15/3 + 4 = 5 + 4 = 9.
   Final Answer: f(3) = 9.00.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 1 2 4
# 1 4 16
# 3
