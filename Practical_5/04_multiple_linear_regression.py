# Multiple Linear Regression
import numpy as np

# User Input Dataset
X1 = np.array(list(map(float, input("Enter X1 (e.g., TV) values (space-separated): ").split())))
X2 = np.array(list(map(float, input("Enter X2 (e.g., Radio) values (space-separated): ").split())))
Y = np.array(list(map(float, input("Enter Y (e.g., Sales) values (space-separated): ").split())))

# Step 1: Form X matrix with a column of 1s for intercept
X = np.column_stack((np.ones(len(X1)), X1, X2))

# Step 2: Convert Y to column vector
Y = Y.reshape(-1, 1)

# Step 3: Apply Normal Equation: b = (X^T X)^(-1) X^T Y
b = np.linalg.inv(X.T @ X) @ X.T @ Y

# Step 4: Extract coefficients
a, b1, b2 = b.flatten()

print(f"Intercept (a): {a:.3f}")
print(f"Coefficient for X1 (b1): {b1:.3f}")
print(f"Coefficient for X2 (b2): {b2:.3f}")
print(f"Regression Equation: Y = {a:.3f} + {b1:.3f}*X1 + {b2:.3f}*X2")

# Step 5: Predict for a new example
X1_new = float(input("Enter new X1 value to predict Y: "))
X2_new = float(input("Enter new X2 value to predict Y: "))
Y_pred = a + b1 * X1_new + b2 * X2_new
print(f"\nPredicted Y for X1={X1_new}, X2={X2_new} -> {Y_pred:.2f}")


"""

================================================================================
THEORY: MULTIPLE LINEAR REGRESSION
================================================================================

1. AIM OF THE MATH CONCEPT:
   To model a dependent variable Y as a linear combination of two or more
   independent variables (X1, X2, ...) using the Normal Equation.

2. FORMULA:
   Y = a + b1*X1 + b2*X2 + ... + bn*Xn
   b = (X^T * X)^(-1) * X^T * Y

3. TERMS OF FORMULA:
   - X : Design matrix with a column of 1s for the intercept.
   - Y : Output column vector.
   - b : Coefficient vector [a, b1, b2, ...]^T.

4. DEFINITION:
   Multiple Linear Regression extends simple linear regression to multiple
   predictors using matrix-based Ordinary Least Squares.

5. THEORY RELATED:
   Requires X^T * X to be non-singular (no perfect multicollinearity).

6. REAL-LIFE APPLICATIONS:
   - Marketing mix modeling (TV + Radio spend -> Sales).
   - Real estate pricing (Area + Bedrooms + Location -> Price).

7. EXAMPLES:
   X1 = [230, 44, 17, 151, 180], X2 = [37, 39, 45, 41, 10], Y = [22, 10, 9, 18, 13].

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Using the dataset above:
   Step 1: Construct X = [[1,230,37], [1,44,39], [1,17,45], [1,151,41], [1,180,10]].
   Step 2: Compute b = (X^T X)^(-1) X^T Y:
       a = -1.528,  b1 = 0.069,  b2 = 0.214.
   Step 3: Predict for X1 = 100, X2 = 30:
       Y_pred = -1.528 + 0.069(100) + 0.214(30) = -1.528 + 6.9 + 6.42 = 11.79.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 230 44 17 151 180
# 37 39 45 41 10
# 22 10 9 18 13
# 100
# 30
