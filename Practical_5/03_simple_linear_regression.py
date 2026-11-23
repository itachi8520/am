# Simple Linear Regression
import numpy as np
import matplotlib.pyplot as plt

# User Input Dataset
x = np.array(list(map(float, input("Enter X values (space-separated): ").split())))
y = np.array(list(map(float, input("Enter Y values (space-separated): ").split())))

# Step 1: Calculate means
x_mean = np.mean(x)
y_mean = np.mean(y)

# Step 2: Calculate slope (b) and intercept (a)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
b = numerator / denominator
a = y_mean - b * x_mean

print(f"Slope (b) = {b:.2f}")
print(f"Intercept (a) = {a:.2f}")
print(f"Equation of regression line: Y = {a:.2f} + {b:.2f}X")

# Step 3: Predicted values
y_pred = a + b * x
print(y_pred)

# Step 4: Plot
plt.scatter(x, y, color='blue', label='Actual data')
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Linear Regression (Manual Calculation)')
plt.legend()
plt.grid(True)
plt.show()


"""

================================================================================
THEORY: SIMPLE LINEAR REGRESSION
================================================================================

1. AIM OF THE MATH CONCEPT:
   To find the straight line of best fit (Y = a + bX) that models the linear
   relationship between independent variable X and dependent variable Y.

2. FORMULA:
   Y = a + b * X
   b = sum((x - x_mean) * (y - y_mean)) / sum((x - x_mean)^2)
   a = y_mean - b * x_mean

3. TERMS OF FORMULA:
   - Y : Dependent variable.
   - X : Independent variable.
   - b : Slope of the regression line.
   - a : Y-intercept.

4. DEFINITION:
   Simple Linear Regression fits a linear equation to observed data by
   minimizing the sum of squared residuals (Ordinary Least Squares).

5. THEORY RELATED:
   The regression line always passes through the centroid (x_mean, y_mean).

6. REAL-LIFE APPLICATIONS:
   - Predicting house prices from area, forecasting sales from ad budget.

7. EXAMPLES:
   x = [10, 20, 30, 40, 50], y = [25, 45, 65, 75, 95] -> Y = 10.00 + 1.70X.

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Given x = [10, 20, 30, 40, 50], y = [25, 45, 65, 75, 95]:
   Step 1: Means: x_mean = 30, y_mean = 61.
   Step 2: Numerator = (-20)(-36) + (-10)(-16) + (0)(4) + (10)(14) + (20)(34)
                     = 720 + 160 + 0 + 140 + 680 = 1700.
   Step 3: Denominator = 400 + 100 + 0 + 100 + 400 = 1000.
   Step 4: Slope b = 1700 / 1000 = 1.70.
   Step 5: Intercept a = 61 - (1.70 * 30) = 61 - 51 = 10.00.
   Final Equation: Y = 10.00 + 1.70X.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 10 20 30 40 50
# 25 45 65 75 95
