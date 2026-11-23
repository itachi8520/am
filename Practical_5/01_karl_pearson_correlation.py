# Karl Pearson's Coefficient of Correlation
import numpy as np

# User Input
x = np.array(list(map(float, input("Enter X values (space-separated): ").split())))
y = np.array(list(map(float, input("Enter Y values (space-separated): ").split())))

# Calculate Pearson correlation coefficient
mean_x = np.mean(x)
mean_y = np.mean(y)

numerator = np.sum((x - mean_x) * (y - mean_y))
denominator = np.sqrt(np.sum((x - mean_x) ** 2) * np.sum((y - mean_y) ** 2))
r = numerator / denominator

print("Karl Pearson's Coefficient of Correlation (r):", round(r, 2))


"""

================================================================================
THEORY: KARL PEARSON'S COEFFICIENT OF CORRELATION
================================================================================

1. AIM OF THE MATH CONCEPT:
   To measure the strength and direction of the linear relationship between two
   variables X and Y.

2. FORMULA:
   r = sum((x_i - x_bar)*(y_i - y_bar)) / sqrt(sum((x_i - x_bar)^2) * sum((y_i - y_bar)^2))

3. TERMS OF FORMULA:
   - r            : Correlation coefficient (-1 <= r <= 1).
   - x_i, y_i     : Observed values of X and Y.
   - x_bar, y_bar : Means of X and Y.

4. DEFINITION:
   Karl Pearson's correlation coefficient quantifies the degree of linear
   association between two continuous variables.

5. THEORY RELATED:
   r = +1 (perfect positive), r = -1 (perfect negative), r = 0 (no linear correlation).

6. REAL-LIFE APPLICATIONS:
   - Stock portfolio diversification, advertising spend vs. revenue, age vs. BP.

7. EXAMPLES:
   x = [5, 20, 30, 40, 50], y = [30, 50, 55, 60, 70] -> r = 0.98.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Given X = [1, 2, 3], Y = [2, 4, 6]:
   Step 1: Means: x_bar = 2, y_bar = 4.
   Step 2: Deviations: (x - x_bar) = [-1, 0, 1], (y - y_bar) = [-2, 0, 2].
   Step 3: Numerator = (-1)(-2) + (0)(0) + (1)(2) = 4.
   Step 4: Denominator = sqrt((1+0+1) * (4+0+4)) = sqrt(16) = 4.
   Step 5: r = 4 / 4 = 1.0 (perfect positive linear correlation).
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 1 2 3 4 5
# 2 4 5 4 5
