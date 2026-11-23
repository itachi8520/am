# Implement Newton's Interpolation method
import numpy as np
import math

# Function to calculate forward differences
def forward_diff_table(y):
    n = len(y)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]
    return diff_table

# Function to evaluate Newton polynomial at x_val
def newton_forward_interpolation(x, y, x_val):
    h = x[1] - x[0]  # uniform spacing
    diff_table = forward_diff_table(y)
    u = (x_val - x[0]) / h
    result = y[0]
    u_term = 1
    for i in range(1, len(y)):
        u_term *= (u - (i - 1))
        result += (u_term / math.factorial(i)) * diff_table[0][i]
    return result

# User Input data
x = np.array(list(map(float, input("Enter equally spaced x values (space-separated): ").split())))
y = np.array(list(map(float, input("Enter corresponding y values (space-separated): ").split())))

# Value to estimate
x_val = float(input("Enter value of x to estimate: "))

# Apply Newton's Interpolation
y_pred = newton_forward_interpolation(x, y, x_val)
print(f"Estimated value of f({x_val}) = {y_pred:.2f}")


"""

================================================================================
THEORY: NEWTON'S FORWARD INTERPOLATION METHOD
================================================================================

1. AIM OF THE MATH CONCEPT:
   To estimate f(x) near the beginning of a table of equally spaced data points.

2. FORMULA:
   f(x) = y0 + u*Delta(y0) + (u*(u-1)/2!)*Delta^2(y0) + ...
   where u = (x - x0) / h

3. TERMS OF FORMULA:
   - h          : Uniform step size (x1 - x0).
   - u          : Normalized distance (x - x0) / h.
   - Delta^k(y) : k-th forward difference.

4. DEFINITION:
   Newton's Forward Interpolation uses finite forward differences to construct
   an interpolating polynomial for uniformly spaced data.

5. THEORY RELATED:
   Most accurate near the start of the table.

6. REAL-LIFE APPLICATIONS:
   - Census population interpolation, hourly weather estimation, yield curves.

7. EXAMPLES:
   x = [5, 7, 9, 11], y = [150, 392, 1452, 2366], x_val = 10 -> f(10) = 1987.50.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Given x = [0, 1, 2], y = [1, 2, 5], estimate f(0.5):
   Step 1: h = 1 - 0 = 1,  u = (0.5 - 0) / 1 = 0.5.
   Step 2: Forward differences:
       Delta(y0) = 2 - 1 = 1,  Delta(y1) = 5 - 2 = 3.
       Delta^2(y0) = 3 - 1 = 2.
   Step 3: Apply formula:
       f(0.5) = 1 + (0.5)(1) + ((0.5)(-0.5) / 2) * 2
              = 1 + 0.5 - 0.25 = 1.25.
   Final Answer: f(0.5) = 1.25.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 0 1 2
# 1 2 5
# 0.5
