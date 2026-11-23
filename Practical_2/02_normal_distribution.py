# Demonstrate Normal Distribution
import math
import numpy as np
import matplotlib.pyplot as plt

def normal_pdf(x, mu, sigma):
    coeff = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
    return coeff * math.exp(exponent)

# User Input Parameters
mu = float(input("Enter mean (mu, e.g., 0): "))
sigma = float(input("Enter standard deviation (sigma, e.g., 1): "))
x_min = float(input("Enter minimum x value (e.g., -4): "))
x_max = float(input("Enter maximum x value (e.g., 4): "))
num_points = int(input("Enter number of points (e.g., 100): "))

# Generate x values
x_values = np.linspace(x_min, x_max, num_points)
print(x_values)

pdf_values = [normal_pdf(x, mu, sigma) for x in x_values]
print(pdf_values)

# Plotting
plt.plot(x_values, pdf_values)
plt.title('Normal Distribution PDF (without built-in functions)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()


"""

================================================================================
THEORY: NORMAL DISTRIBUTION (CONTINUOUS RANDOM VARIABLE)
================================================================================

1. AIM OF THE MATH CONCEPT:
   To calculate and plot the Probability Density Function (PDF) of a Normal
   (Gaussian) distribution manually without built-in statistical libraries.

2. FORMULA:
   f(x) = (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sigma)^2)

3. TERMS OF FORMULA:
   - f(x)  : Probability density at point x.
   - mu    : Mean (center of the bell curve).
   - sigma : Standard deviation (spread of the curve, sigma > 0).
   - x     : Continuous variable.

4. DEFINITION:
   The Normal distribution is a symmetric, bell-shaped continuous probability
   distribution defined completely by its mean (mu) and standard deviation (sigma).

5. THEORY RELATED:
   Total area under the curve is 1. Mean = Median = Mode = mu.
   Empirical Rule: 68% of data lies within 1 sigma, 95% within 2 sigma, and
   99.7% within 3 sigma.

6. REAL-LIFE APPLICATIONS:
   - Human height, weight, and IQ scores.
   - Measurement errors in scientific experiments.
   - Financial return modeling and manufacturing tolerances.

7. EXAMPLES:
   Standard Normal Distribution with mu = 0, sigma = 1 over [-4, 4].

8. SOLVED EXAMPLE (STEP-BY-STEP):
   Find the probability density f(x) at x = 1 for a Standard Normal distribution
   (mu = 0, sigma = 1).

   Step 1: Compute coefficient:
       coeff = 1 / (1 * sqrt(2 * 3.14159)) = 1 / 2.50663 = 0.39894.
   Step 2: Compute exponent:
       exponent = -((1 - 0)^2) / (2 * 1^2) = -0.5.
   Step 3: Multiply:
       f(1) = 0.39894 * e^(-0.5) = 0.39894 * 0.60653 = 0.24197.
   Final Answer: f(1) ≈ 0.2420.
================================================================================
"""

# SAMPLE INPUT (one line per prompt)
# 0
# 1
# -4
# 4
# 100
